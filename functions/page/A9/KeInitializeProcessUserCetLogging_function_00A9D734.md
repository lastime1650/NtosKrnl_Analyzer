# KeInitializeProcessUserCetLogging

- RVA: `0x00A9D734`–`0x00A9D7A2` (길이 `110` bytes)
- VA: `0x0000000140A9D734`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005DAC8`
- 디코드: `29`개 명령, `110/110` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A9D74B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)

### Direct callers
- [PspAllocateProcess](../A1/PspAllocateProcess_function_00A13B3C.md) at `0x00A15B4F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A9D74B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A9D734  40 53                           push rbx
00A9D736  48 83 EC 20                     sub rsp, 0x20
00A9D73A  BA C0 00 00 00                  mov edx, 0xc0
00A9D73F  48 8B D9                        mov rbx, rcx
00A9D742  41 B8 43 45 54 4C               mov r8d, 0x4c544543
00A9D748  8D 4A 40                        lea ecx, [rdx + 0x40]
00A9D74B  E8 A0 49 0E 00                  call 0x140b820f0
00A9D750  33 D2                           xor edx, edx
00A9D752  48 85 C0                        test rax, rax
00A9D755  74 44                           je 0x140a9d79b
00A9D757  48 8D 48 58                     lea rcx, [rax + 0x58]
00A9D75B  48 89 10                        mov qword ptr [rax], rdx
00A9D75E  48 89 48 08                     mov qword ptr [rax + 8], rcx
00A9D762  44 8D 42 05                     lea r8d, [rdx + 5]
00A9D766  48 8D 88 80 00 00 00            lea rcx, [rax + 0x80]
00A9D76D  44 89 40 14                     mov dword ptr [rax + 0x14], r8d
00A9D771  48 89 48 20                     mov qword ptr [rax + 0x20], rcx
00A9D775  48 8D 88 A8 00 00 00            lea rcx, [rax + 0xa8]
00A9D77C  48 89 48 38                     mov qword ptr [rax + 0x38], rcx
00A9D780  44 89 40 2C                     mov dword ptr [rax + 0x2c], r8d
00A9D784  C7 40 44 03 00 00 00            mov dword ptr [rax + 0x44], 3
00A9D78B  48 89 83 A8 01 00 00            mov qword ptr [rbx + 0x1a8], rax
00A9D792  8B C2                           mov eax, edx
00A9D794  48 83 C4 20                     add rsp, 0x20
00A9D798  5B                              pop rbx
00A9D799  C3                              ret
00A9D79A  CC                              int3
00A9D79B  BA 17 00 00 C0                  mov edx, 0xc0000017
00A9D7A0  EB F0                           jmp 0x140a9d792
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeInitializeProcessUserCetLogging(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = ExAllocatePool2(192 + 64, 192, (unsigned int)(0x4C544543ULL), a4);
    a2 = 0;
    if (result == 0) goto loc_00A9D79B;
    *(unsigned __int64 *)(result) = 0;
    *(unsigned __int64 *)(result + 8) = result + 88;
    *(unsigned int *)(result + 20) = (unsigned int)(a2 + 5);
    *(unsigned __int64 *)(result + 32) = result + 128;
    *(unsigned __int64 *)(result + 56) = result + 168;
    *(unsigned int *)(result + 44) = (unsigned int)(a2 + 5);
    *(unsigned int *)(result + 68) = 3;
    *(unsigned __int64 *)(a1 + 424) = result;
loc_00A9D792:
    v_rsp = (v_rsp) + (32);
    return 0;
loc_00A9D79B:
    goto loc_00A9D792;
}
```

## 5. (Beta) C Style

```c
int64_t KeInitializeProcessUserCetLogging(void *ProcessUserCetLogging)
{
    uint8_t *processUserCetLogging = (uint8_t *)ProcessUserCetLogging;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = ExAllocatePool2(192 + 64, 192, (uint32_t)(0x4C544543ULL), a4);
    a2 = 0;
    if (result == 0) goto loc_00A9D79B;
    *(uint64_t *)(result) = 0;
    *(uint64_t *)(result + 0x8) = result + 88;
    *(uint32_t *)(result + 0x14) = (uint32_t)(a2 + 5);
    *(uint64_t *)(result + 0x20) = result + 128;
    *(uint64_t *)(result + 0x38) = result + 168;
    *(uint32_t *)(result + 0x2C) = (uint32_t)(a2 + 5);
    *(uint32_t *)(result + 0x44) = 3;
    *(uint64_t *)(processUserCetLogging + 0x1A8) = result;
loc_00A9D792:
    local_rsp = (local_rsp) + (32);
    return 0;
loc_00A9D79B:
    goto loc_00A9D792;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `ProcessUserCetLogging` | `+ 0x1A8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A9D734&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A9D734[BB_00A9D734]
  bb_00A9D757[BB_00A9D757]
  bb_00A9D792[BB_00A9D792]
  bb_00A9D79A[BB_00A9D79A]
  bb_00A9D79B[BB_00A9D79B]
  bb_00A9D734 -->|branch| bb_00A9D79B
  bb_00A9D734 -->|fallthrough| bb_00A9D757
  bb_00A9D757 -->|flow| bb_00A9D792
  bb_00A9D79A -->|flow| bb_00A9D79B
  bb_00A9D79B -->|branch| bb_00A9D792
```
