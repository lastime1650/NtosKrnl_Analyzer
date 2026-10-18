# BapdProcessFwRamdiskInformation

- RVA: `0x00C4F6E8`–`0x00C4F73E` (길이 `86` bytes)
- VA: `0x0000000140C4F6E8`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `22`개 명령, `86/86` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00C4F716` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)

### Direct callers
- [BootApplicationPersistentDataProcess](../BE/BootApplicationPersistentDataProcess_function_00BEEBD4.md) at `0x00BEEC27`

### Static image references
- `0x00C4F6EE` → RVA `0x00FC6B20` (`ALMOSTRO`; read)
- `0x00C4F71B` → RVA `0x00EFF028` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00C4F716` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C4F6E8  40 53                           push rbx
00C4F6EA  48 83 EC 20                     sub rsp, 0x20
00C4F6EE  48 8B 05 2B 74 37 00            mov rax, qword ptr [rip + 0x37742b]
00C4F6F5  48 8B 88 F0 00 00 00            mov rcx, qword ptr [rax + 0xf0]
00C4F6FC  48 8B 99 70 0E 00 00            mov rbx, qword ptr [rcx + 0xe70]
00C4F703  48 85 DB                        test rbx, rbx
00C4F706  74 2F                           je 0x140c4f737
00C4F708  BA 18 00 00 00                  mov edx, 0x18
00C4F70D  41 B8 42 61 50 64               mov r8d, 0x64506142
00C4F713  8D 4A 28                        lea ecx, [rdx + 0x28]
00C4F716  E8 D5 29 F3 FF                  call 0x140b820f0
00C4F71B  48 89 05 06 F9 2A 00            mov qword ptr [rip + 0x2af906], rax
00C4F722  48 85 C0                        test rax, rax
00C4F725  74 10                           je 0x140c4f737
00C4F727  0F 10 03                        movups xmm0, xmmword ptr [rbx]
00C4F72A  0F 11 00                        movups xmmword ptr [rax], xmm0
00C4F72D  F2 0F 10 4B 10                  movsd xmm1, qword ptr [rbx + 0x10]
00C4F732  F2 0F 11 48 10                  movsd qword ptr [rax + 0x10], xmm1
00C4F737  48 83 C4 20                     add rsp, 0x20
00C4F73B  5B                              pop rbx
00C4F73C  C3                              ret
00C4F73D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BapdProcessFwRamdiskInformation(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3634219) + 240) + 3696) == 0) goto loc_00C4F737;
    result = ExAllocatePool2(24 + 40, 24, (unsigned int)(0x64506142ULL), a4);
    *(unsigned __int64 *)(v_rip + 2816262) = result;
    if (result != 0) {
        *(unsigned __int64 *)(result) = v_xmm0;
        *(unsigned __int64 *)(result + 16) = v_xmm1;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
void BapdProcessFwRamdiskInformation(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x37742B) + 0xF0) + 0xE70) == 0) goto loc_00C4F737;
    result = ExAllocatePool2(24 + 40, 24, (uint32_t)(0x64506142ULL), a4);
    *(uint64_t *)(v_rip + 0x2AF906) = result;
    if (result != 0) {
        *(uint64_t *)(result) = v_xmm0;
        *(uint64_t *)(result + 0x10) = v_xmm1;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C4F6E8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C4F6E8[BB_00C4F6E8]
  bb_00C4F708[BB_00C4F708]
  bb_00C4F727[BB_00C4F727]
  bb_00C4F737[BB_00C4F737]
  bb_00C4F73D[BB_00C4F73D]
  bb_00C4F6E8 -->|branch| bb_00C4F737
  bb_00C4F6E8 -->|fallthrough| bb_00C4F708
  bb_00C4F708 -->|branch| bb_00C4F737
  bb_00C4F708 -->|fallthrough| bb_00C4F727
  bb_00C4F727 -->|flow| bb_00C4F737
```
