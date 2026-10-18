# RtlPcToFilePath

- RVA: `0x00A2B9A0`–`0x00A2B9E3` (길이 `67` bytes)
- VA: `0x0000000140A2B9A0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006CF28`
- 디코드: `21`개 명령, `67/67` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A2B9AD` → [MmLockLoadedDataTableEntryShared](../../text/4B/MmLockLoadedDataTableEntryShared_function_004BD08C.md) (function, `0x004BD08C`)
- `0x00A2B9C1` → [RtlCopyUnicodeString](../../text/3F/RtlCopyUnicodeString_function_003FEF30.md) (function, `0x003FEF30`)
- `0x00A2B9C9` → [MmUnlockLoadedDataTableEntryShared](../../text/4B/MmUnlockLoadedDataTableEntryShared_function_004BE49C.md) (function, `0x004BE49C`)

### Direct callers
- [KitLogFeatureUsage](../../text/65/KitLogFeatureUsage_function_0065C030.md) at `0x0065C0E9`
- [EtwpProviderArrivalCallback](../A0/EtwpProviderArrivalCallback_function_00A03F94.md) at `0x00A04022`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00A2B9AD` → [MmLockLoadedDataTableEntryShared](../../text/4B/MmLockLoadedDataTableEntryShared_function_004BD08C.md) (`PAGE` → `.text`)
  - `0x00A2B9C1` → [RtlCopyUnicodeString](../../text/3F/RtlCopyUnicodeString_function_003FEF30.md) (`PAGE` → `.text`)
  - `0x00A2B9C9` → [MmUnlockLoadedDataTableEntryShared](../../text/4B/MmUnlockLoadedDataTableEntryShared_function_004BE49C.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A2B9A0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A2B9A5  57                              push rdi
00A2B9A6  48 83 EC 20                     sub rsp, 0x20
00A2B9AA  48 8B FA                        mov rdi, rdx
00A2B9AD  E8 DA 16 A9 FF                  call 0x1404bd08c
00A2B9B2  48 8B D8                        mov rbx, rax
00A2B9B5  48 85 C0                        test rax, rax
00A2B9B8  74 22                           je 0x140a2b9dc
00A2B9BA  48 8D 50 48                     lea rdx, [rax + 0x48]
00A2B9BE  48 8B CF                        mov rcx, rdi
00A2B9C1  E8 6A 35 9D FF                  call 0x1403fef30
00A2B9C6  48 8B CB                        mov rcx, rbx
00A2B9C9  E8 CE 2A A9 FF                  call 0x1404be49c
00A2B9CE  33 C0                           xor eax, eax
00A2B9D0  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00A2B9D5  48 83 C4 20                     add rsp, 0x20
00A2B9D9  5F                              pop rdi
00A2B9DA  C3                              ret
00A2B9DB  CC                              int3
00A2B9DC  B8 25 02 00 C0                  mov eax, 0xc0000225
00A2B9E1  EB ED                           jmp 0x140a2b9d0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlPcToFilePath(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = MmLockLoadedDataTableEntryShared(a1, a2, a3, a4);
    if (result == 0) goto loc_00A2B9DC;
    result = RtlCopyUnicodeString(a2, result + 72, a3, a4);
    result = MmUnlockLoadedDataTableEntryShared(result, result + 72, a3, a4);
    result = 0;
loc_00A2B9D0:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00A2B9DC:
    goto loc_00A2B9D0;
}
```

## 5. (Beta) C Style

```c
int64_t RtlPcToFilePath(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = MmLockLoadedDataTableEntryShared(Arg1, Arg2, a3, a4);
    if (result == 0) goto loc_00A2B9DC;
    result = RtlCopyUnicodeString(Arg2, result + 72, a3, a4);
    result = MmUnlockLoadedDataTableEntryShared(result, result + 72, a3, a4);
    result = 0;
loc_00A2B9D0:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00A2B9DC:
    goto loc_00A2B9D0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A2B9A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A2B9A0[BB_00A2B9A0]
  bb_00A2B9BA[BB_00A2B9BA]
  bb_00A2B9D0[BB_00A2B9D0]
  bb_00A2B9DB[BB_00A2B9DB]
  bb_00A2B9DC[BB_00A2B9DC]
  bb_00A2B9A0 -->|branch| bb_00A2B9DC
  bb_00A2B9A0 -->|fallthrough| bb_00A2B9BA
  bb_00A2B9BA -->|flow| bb_00A2B9D0
  bb_00A2B9DB -->|flow| bb_00A2B9DC
  bb_00A2B9DC -->|branch| bb_00A2B9D0
```
