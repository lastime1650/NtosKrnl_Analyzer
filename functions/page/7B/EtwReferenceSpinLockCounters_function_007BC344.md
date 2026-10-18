# EtwReferenceSpinLockCounters

- RVA: `0x007BC344`–`0x007BC3A3` (길이 `95` bytes)
- VA: `0x00000001407BC344`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `23`개 명령, `95/95` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x007BC35D` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x007BC38A` → [EtwpUpdateGlobalGroupMasks](../A4/EtwpUpdateGlobalGroupMasks_function_00A4F55C.md) (function, `0x00A4F55C`)
- `0x007BC398` → [KeReleaseMutex](../../text/39/KeReleaseMutex_function_00396810.md) (function, `0x00396810`)

### Direct callers
- [KiSynchCounterSetCallback](../A5/KiSynchCounterSetCallback_function_00A5F5B0.md) at `0x00A5F6EC`
- [KiSynchNumaCounterSetCallback](../A7/KiSynchNumaCounterSetCallback_function_00A77BE0.md) at `0x00A781A5`

### Static image references
- `0x007BC34E` → RVA `0x00EFF7E0` (`.data`; read)
- `0x007BC362` → RVA `0x00FD80D4` (`PAGEDATA`; read)
- `0x007BC36A` → RVA `0x00FD80D4` (`PAGEDATA`; write)
- `0x007BC375` → RVA `0x00FC6AA8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x007BC35D` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x007BC398` → [KeReleaseMutex](../../text/39/KeReleaseMutex_function_00396810.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007BC344  48 83 EC 38                     sub rsp, 0x38
007BC348  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
007BC34E  48 8D 0D 8B 34 74 00            lea rcx, [rip + 0x74348b]
007BC355  45 33 C9                        xor r9d, r9d
007BC358  45 33 C0                        xor r8d, r8d
007BC35B  33 D2                           xor edx, edx
007BC35D  E8 4E 23 A5 FF                  call 0x14020e6b0
007BC362  8B 05 6C BD 81 00               mov eax, dword ptr [rip + 0x81bd6c]
007BC368  FF C0                           inc eax
007BC36A  89 05 64 BD 81 00               mov dword ptr [rip + 0x81bd64], eax
007BC370  83 F8 01                        cmp eax, 1
007BC373  75 1A                           jne 0x1407bc38f
007BC375  48 8B 0D 2C A7 80 00            mov rcx, qword ptr [rip + 0x80a72c]
007BC37C  44 8D 40 07                     lea r8d, [rax + 7]
007BC380  33 D2                           xor edx, edx
007BC382  0F BA A9 D0 12 00 00 15         bts dword ptr [rcx + 0x12d0], 0x15
007BC38A  E8 CD 31 29 00                  call 0x140a4f55c
007BC38F  33 D2                           xor edx, edx
007BC391  48 8D 0D 48 34 74 00            lea rcx, [rip + 0x743448]
007BC398  E8 73 A4 BD FF                  call 0x140396810
007BC39D  48 83 C4 38                     add rsp, 0x38
007BC3A1  C3                              ret
007BC3A2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwReferenceSpinLockCounters(__int64 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(v_rip + 7615627, a2, a3, a4);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 8502636))) + 1);
    *(unsigned int *)(v_rip + 8502628) = (unsigned int)(result);
    if (((unsigned int)(result)) == 1) {
        a1 = *(unsigned __int64 *)(v_rip + 8431404);
        a3 = result + 7;
        a2 = 0;
        result = EtwpUpdateGlobalGroupMasks(a1, a2, a3, a4);
    }
    a2 = 0;
    result = KeReleaseMutex(v_rip + 7615560, a2, a3, a4);
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwReferenceSpinLockCounters(int64_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    Arg4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(v_rip + 7615627, Arg2, Arg3, Arg4);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x81BD6C))) + 1);
    *(uint32_t *)(v_rip + 0x81BD64) = (uint32_t)(result);
    if (((uint32_t)(result)) == 1) {
        Arg1 = *(uint64_t *)(v_rip + 0x80A72C);
        Arg3 = result + 7;
        Arg2 = 0;
        result = EtwpUpdateGlobalGroupMasks(Arg1, Arg2, Arg3, Arg4);
    }
    Arg2 = 0;
    result = KeReleaseMutex(v_rip + 7615560, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007BC344&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007BC344[BB_007BC344]
  bb_007BC375[BB_007BC375]
  bb_007BC38F[BB_007BC38F]
  bb_007BC3A2[BB_007BC3A2]
  bb_007BC344 -->|branch| bb_007BC38F
  bb_007BC344 -->|fallthrough| bb_007BC375
  bb_007BC375 -->|flow| bb_007BC38F
```
