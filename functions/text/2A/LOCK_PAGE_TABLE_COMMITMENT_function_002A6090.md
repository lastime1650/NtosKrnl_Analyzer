# LOCK_PAGE_TABLE_COMMITMENT

- RVA: `0x002A6090`–`0x002A60E4` (길이 `84` bytes)
- VA: `0x00000001402A6090`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `25`개 명령, `84/84` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **13**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002A60B1` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x002A60CA` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)

### Direct callers
- [MiDeleteEmptyPageTables](MiDeleteEmptyPageTables_function_002A5220.md) at `0x002A546B`
- [MiPerformVadSplitting](MiPerformVadSplitting_function_002A5A80.md) at `0x002A5B7B`
- [MiSplitPrivatePage](MiSplitPrivatePage_function_002A6210.md) at `0x002A651D`
- [MiCommitPageTableRangesForVad](MiCommitPageTableRangesForVad_function_002A69D4.md) at `0x002A6A38`
- [MmOutSwapWorkingSet](MmOutSwapWorkingSet_function_002A6BC8.md) at `0x002A6E35`
- [MmOutSwapVirtualAddresses](MmOutSwapVirtualAddresses_function_002A8C30.md) at `0x002A8E04`
- [sub_002C3A7C](../2C/Unknown_function_002C3A7C.md) at `0x002C3AE5`
- [MiSplitReducedCommitClonePage](../4F/MiSplitReducedCommitClonePage_function_004FA808.md) at `0x004FA879`
- [MmAssignProcessToJob](../../page/87/MmAssignProcessToJob_function_0087EEF8.md) at `0x0087EF84`
- [MiFreeToSubAllocatedRegion](../../page/87/MiFreeToSubAllocatedRegion_function_0087FB7C.md) at `0x0087FBF7`
- [MiInsertVadCharges](../../page/88/MiInsertVadCharges_function_00886AA8.md) at `0x00886B8F`
- [MiAllocateFromSubAllocatedRegion](../../page/98/MiAllocateFromSubAllocatedRegion_function_00981C24.md) at `0x00981CAC`
- [MiAllocateNewSubAllocatedRegion](../../page/98/MiAllocateNewSubAllocatedRegion_function_00981EC0.md) at `0x00982142`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002A6090  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
002A6095  57                              push rdi
002A6096  48 83 EC 20                     sub rsp, 0x20
002A609A  66 FF 89 E6 01 00 00            dec word ptr [rcx + 0x1e6]
002A60A1  48 8D BA 60 02 00 00            lea rdi, [rdx + 0x260]
002A60A8  48 8B CF                        mov rcx, rdi
002A60AB  45 33 C0                        xor r8d, r8d
002A60AE  33 D2                           xor edx, edx
002A60B0  90                              nop
002A60B1  E8 7A A1 F6 FF                  call 0x140210230
002A60B6  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
002A60BC  48 8B D8                        mov rbx, rax
002A60BF  73 0E                           jae 0x1402a60cf
002A60C1  4C 8B C7                        mov r8, rdi
002A60C4  48 8B D0                        mov rdx, rax
002A60C7  48 8B CF                        mov rcx, rdi
002A60CA  E8 C1 9B F6 FF                  call 0x14020fc90
002A60CF  48 85 DB                        test rbx, rbx
002A60D2  74 04                           je 0x1402a60d8
002A60D4  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
002A60D8  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
002A60DD  48 83 C4 20                     add rsp, 0x20
002A60E1  5F                              pop rdi
002A60E2  C3                              ret
002A60E3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall LOCK_PAGE_TABLE_COMMITMENT(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a2 + 608, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = a2 + 608;
        a2 = result;
        a1 = a2 + 608;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t LOCK_PAGE_TABLE_COMMITMENT(void *Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg2 + 608, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg2 + 608;
        Arg2 = result;
        Arg1 = Arg2 + 608;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1E6` | `16` | `R/W` |
| `Arg2` | `+ 0x0` | `64` | `R/W` |
| `Arg2` | `+ 0x260` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002A6090&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002A6090[BB_002A6090]
  bb_002A60C1[BB_002A60C1]
  bb_002A60CF[BB_002A60CF]
  bb_002A60D4[BB_002A60D4]
  bb_002A60D8[BB_002A60D8]
  bb_002A60E3[BB_002A60E3]
  bb_002A6090 -->|branch| bb_002A60CF
  bb_002A6090 -->|fallthrough| bb_002A60C1
  bb_002A60C1 -->|flow| bb_002A60CF
  bb_002A60CF -->|branch| bb_002A60D8
  bb_002A60CF -->|fallthrough| bb_002A60D4
  bb_002A60D4 -->|flow| bb_002A60D8
```
