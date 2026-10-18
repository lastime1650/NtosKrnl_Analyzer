# MmInitSystemDll

- RVA: `0x00BEEFB0`–`0x00BEEFF7` (길이 `71` bytes)
- VA: `0x0000000140BEEFB0`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `21`개 명령, `71/71` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00BEEFB8` → [PsQuerySystemDllInfo](../../page/8D/PsQuerySystemDllInfo_function_008D20F8.md) (function, `0x008D20F8`)
- `0x00BEEFC9` → [PspReferenceSystemDll](../../page/8D/PspReferenceSystemDll_function_008D6AD8.md) (function, `0x008D6AD8`)
- `0x00BEEFEB` → [ObFastDereferenceObject](../../text/3E/ObFastDereferenceObject_function_003ED5F0.md) (function, `0x003ED5F0`)

### Direct callers
- [Phase1InitializationIoReady](../C7/Phase1InitializationIoReady_function_00C70458.md) at `0x00C7063A`

### Static image references
- `0x00BEEFD2` → RVA `0x00E2DB40` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00BEEFB8` → [PsQuerySystemDllInfo](../../page/8D/PsQuerySystemDllInfo_function_008D20F8.md) (`INIT` → `PAGE`)
  - `0x00BEEFC9` → [PspReferenceSystemDll](../../page/8D/PspReferenceSystemDll_function_008D6AD8.md) (`INIT` → `PAGE`)
  - `0x00BEEFEB` → [ObFastDereferenceObject](../../text/3E/ObFastDereferenceObject_function_003ED5F0.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BEEFB0  40 53                           push rbx
00BEEFB2  48 83 EC 20                     sub rsp, 0x20
00BEEFB6  33 C9                           xor ecx, ecx
00BEEFB8  E8 3B 31 CE FF                  call 0x1408d20f8
00BEEFBD  48 8B D8                        mov rbx, rax
00BEEFC0  48 85 C0                        test rax, rax
00BEEFC3  74 2B                           je 0x140beeff0
00BEEFC5  48 8B 48 F8                     mov rcx, qword ptr [rax - 8]
00BEEFC9  E8 0A 7B CE FF                  call 0x1408d6ad8
00BEEFCE  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
00BEEFD2  48 89 0D 67 EB 23 00            mov qword ptr [rip + 0x23eb67], rcx
00BEEFD9  48 85 C0                        test rax, rax
00BEEFDC  74 12                           je 0x140beeff0
00BEEFDE  48 8B 4B F8                     mov rcx, qword ptr [rbx - 8]
00BEEFE2  41 B8 50 73 53 64               mov r8d, 0x64537350
00BEEFE8  48 8B D0                        mov rdx, rax
00BEEFEB  E8 00 E6 7F FF                  call 0x1403ed5f0
00BEEFF0  48 83 C4 20                     add rsp, 0x20
00BEEFF4  5B                              pop rbx
00BEEFF5  C3                              ret
00BEEFF6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmInitSystemDll(int a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a1 = 0;
    result = PsQuerySystemDllInfo(a1, a2, a3, a4);
    if (result == 0) goto loc_00BEEFF0;
    result = PspReferenceSystemDll(*(unsigned __int64 *)(result - 8), a2, a3, a4);
    *(unsigned __int64 *)(v_rip + 2354023) = *(unsigned __int64 *)(result + 24);
    if (result != 0) {
        a1 = *(unsigned __int64 *)(result - 8);
        a3 = 0x64537350ULL;
        a2 = result;
        result = ObFastDereferenceObject(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MmInitSystemDll(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg1 = 0;
    result = PsQuerySystemDllInfo(Arg1, a2, a3, a4);
    if (result == 0) goto loc_00BEEFF0;
    result = PspReferenceSystemDll(*(uint64_t *)(result - 0x8), a2, a3, a4);
    *(uint64_t *)(v_rip + 0x23EB67) = *(uint64_t *)(result + 0x18);
    if (result != 0) {
        Arg1 = *(uint64_t *)(result - 0x8);
        a3 = 0x64537350ULL;
        a2 = result;
        result = ObFastDereferenceObject(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00BEEFB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BEEFB0[BB_00BEEFB0]
  bb_00BEEFC5[BB_00BEEFC5]
  bb_00BEEFDE[BB_00BEEFDE]
  bb_00BEEFF0[BB_00BEEFF0]
  bb_00BEEFF6[BB_00BEEFF6]
  bb_00BEEFB0 -->|branch| bb_00BEEFF0
  bb_00BEEFB0 -->|fallthrough| bb_00BEEFC5
  bb_00BEEFC5 -->|branch| bb_00BEEFF0
  bb_00BEEFC5 -->|fallthrough| bb_00BEEFDE
  bb_00BEEFDE -->|flow| bb_00BEEFF0
```
