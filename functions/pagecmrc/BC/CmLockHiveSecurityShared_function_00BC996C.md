# CmLockHiveSecurityShared

- RVA: `0x00BC996C`–`0x00BC99C0` (길이 `84` bytes)
- VA: `0x0000000140BC996C`
- 실행 섹션: `PAGECMRC`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068D5C`
- 디코드: `26`개 명령, `84/84` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **10**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BC9985` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00BC99A6` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)

### Direct callers
- [CmDumpKeyToFile](../../page/7D/CmDumpKeyToFile_function_007DCD64.md) at `0x007DCDFD`
- [CmSaveMergedKeys](../../page/7D/CmSaveMergedKeys_function_007DE040.md) at `0x007DE1D2`
- [CmSaveMergedKeys](../../page/7D/CmSaveMergedKeys_function_007DE040.md) at `0x007DE20D`
- [CmpRebuildKcbCacheFromNode](../../page/84/CmpRebuildKcbCacheFromNode_function_0084C5A8.md) at `0x0084C67B`
- [CmpCreateKeyControlBlock](../../page/85/CmpCreateKeyControlBlock_function_00851DB0.md) at `0x00852242`
- [CmpCreateChild](../../page/94/CmpCreateChild_function_0094817C.md) at `0x00948688`
- [CmpLightWeightCommitSetSecDescUoW](../../page/94/CmpLightWeightCommitSetSecDescUoW_function_0094B4AC.md) at `0x0094B55A`
- [sub_009DA74E](../../page/9D/Unknown_function_009DA74E.md) at `0x009DA75F`
- [CmpLockTwoSecurityCachesExclusiveShared](../../page/A4/CmpLockTwoSecurityCachesExclusiveShared_function_00A45A94.md) at `0x00A45AB1`
- [CmpLockTwoSecurityCachesExclusiveShared](../../page/A4/CmpLockTwoSecurityCachesExclusiveShared_function_00A45A94.md) at `0x00A45AC7`
- [CmpLightWeightCommitAddKeyUoW](../../page/A5/CmpLightWeightCommitAddKeyUoW_function_00A54CA8.md) at `0x00A54D2E`
- [CmpDumpKeyToBuffer](CmpDumpKeyToBuffer_function_00BC9130.md) at `0x00BC91EA`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00BC9985` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGECMRC` → `.text`)
  - `0x00BC99A6` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGECMRC` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BC996C  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00BC9971  57                              push rdi
00BC9972  48 83 EC 20                     sub rsp, 0x20
00BC9976  48 8D B9 F8 06 00 00            lea rdi, [rcx + 0x6f8]
00BC997D  45 33 C0                        xor r8d, r8d
00BC9980  48 8B CF                        mov rcx, rdi
00BC9983  33 D2                           xor edx, edx
00BC9985  E8 A6 68 64 FF                  call 0x140210230
00BC998A  48 8B D8                        mov rbx, rax
00BC998D  B9 11 00 00 00                  mov ecx, 0x11
00BC9992  33 C0                           xor eax, eax
00BC9994  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
00BC9999  74 10                           je 0x140bc99ab
00BC999B  4C 8B CF                        mov r9, rdi
00BC999E  4C 8B C3                        mov r8, rbx
00BC99A1  33 D2                           xor edx, edx
00BC99A3  48 8B CF                        mov rcx, rdi
00BC99A6  E8 A1 6A 64 FF                  call 0x14021044c
00BC99AB  48 85 DB                        test rbx, rbx
00BC99AE  74 04                           je 0x140bc99b4
00BC99B0  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
00BC99B4  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
00BC99B9  48 83 C4 20                     add rsp, 0x20
00BC99BD  5F                              pop rdi
00BC99BE  C3                              ret
00BC99BF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmLockHiveSecurityShared(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 1784, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = a1 + 1784;
        a3 = 0;
        a2 = 0;
        a1 = a1 + 1784;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
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
int64_t CmLockHiveSecurityShared(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 1784, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = Arg1 + 1784;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = Arg1 + 1784;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
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
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x6F8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagecmrc&rva=0x00BC996C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BC996C[BB_00BC996C]
  bb_00BC999B[BB_00BC999B]
  bb_00BC99AB[BB_00BC99AB]
  bb_00BC99B0[BB_00BC99B0]
  bb_00BC99B4[BB_00BC99B4]
  bb_00BC99BF[BB_00BC99BF]
  bb_00BC996C -->|branch| bb_00BC99AB
  bb_00BC996C -->|fallthrough| bb_00BC999B
  bb_00BC999B -->|flow| bb_00BC99AB
  bb_00BC99AB -->|branch| bb_00BC99B4
  bb_00BC99AB -->|fallthrough| bb_00BC99B0
  bb_00BC99B0 -->|flow| bb_00BC99B4
```
