# CmLockHiveSecurityExclusive

- RVA: `0x0084B1A8`–`0x0084B1F4` (길이 `76` bytes)
- VA: `0x000000014084B1A8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `23`개 명령, `76/76` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0084B1C1` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0084B1DA` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)

### Direct callers
- [CmpCreateTombstone](../../text/66/CmpCreateTombstone_function_0066AF50.md) at `0x0066B0C4`
- [CmpAssignKeySecurity](../7E/CmpAssignKeySecurity_function_007EC8B0.md) at `0x007EC954`
- [CmpFreeKeyByCell](CmpFreeKeyByCell_function_0084AD70.md) at `0x0084ADAB`
- [CmpCopyMergeOfLayeredKeyNode](../94/CmpCopyMergeOfLayeredKeyNode_function_00945A78.md) at `0x00945BFC`
- [CmpCreateChild](../94/CmpCreateChild_function_0094817C.md) at `0x0094856F`
- [CmpCreateChild](../94/CmpCreateChild_function_0094817C.md) at `0x00948CD2`
- [CmpSetKeySecurity](../94/CmpSetKeySecurity_function_0094A124.md) at `0x0094A333`
- [CmpUndoDeleteKeyForTrans](../94/CmpUndoDeleteKeyForTrans_function_0094A728.md) at `0x0094A92E`
- [CmpLockTwoSecurityCachesExclusiveShared](../A4/CmpLockTwoSecurityCachesExclusiveShared_function_00A45A94.md) at `0x00A45AA9`
- [CmpLockTwoSecurityCachesExclusiveShared](../A4/CmpLockTwoSecurityCachesExclusiveShared_function_00A45A94.md) at `0x00A45ACF`
- [CmpCreateHiveRootCell](../AB/CmpCreateHiveRootCell_function_00ABF568.md) at `0x00ABF6ED`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0084B1C1` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0084B1DA` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0084B1A8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0084B1AD  57                              push rdi
0084B1AE  48 83 EC 20                     sub rsp, 0x20
0084B1B2  48 8D B9 F8 06 00 00            lea rdi, [rcx + 0x6f8]
0084B1B9  45 33 C0                        xor r8d, r8d
0084B1BC  48 8B CF                        mov rcx, rdi
0084B1BF  33 D2                           xor edx, edx
0084B1C1  E8 6A 50 9C FF                  call 0x140210230
0084B1C6  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
0084B1CC  48 8B D8                        mov rbx, rax
0084B1CF  73 0E                           jae 0x14084b1df
0084B1D1  4C 8B C7                        mov r8, rdi
0084B1D4  48 8B D0                        mov rdx, rax
0084B1D7  48 8B CF                        mov rcx, rdi
0084B1DA  E8 B1 4A 9C FF                  call 0x14020fc90
0084B1DF  48 85 DB                        test rbx, rbx
0084B1E2  74 04                           je 0x14084b1e8
0084B1E4  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
0084B1E8  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0084B1ED  48 83 C4 20                     add rsp, 0x20
0084B1F1  5F                              pop rdi
0084B1F2  C3                              ret
0084B1F3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmLockHiveSecurityExclusive(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 1784, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = a1 + 1784;
        a2 = result;
        a1 = a1 + 1784;
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
int64_t CmLockHiveSecurityExclusive(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 1784, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1 + 1784;
        Arg2 = result;
        Arg1 = Arg1 + 1784;
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
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x6F8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0084B1A8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0084B1A8[BB_0084B1A8]
  bb_0084B1D1[BB_0084B1D1]
  bb_0084B1DF[BB_0084B1DF]
  bb_0084B1E4[BB_0084B1E4]
  bb_0084B1E8[BB_0084B1E8]
  bb_0084B1F3[BB_0084B1F3]
  bb_0084B1A8 -->|branch| bb_0084B1DF
  bb_0084B1A8 -->|fallthrough| bb_0084B1D1
  bb_0084B1D1 -->|flow| bb_0084B1DF
  bb_0084B1DF -->|branch| bb_0084B1E8
  bb_0084B1DF -->|fallthrough| bb_0084B1E4
  bb_0084B1E4 -->|flow| bb_0084B1E8
```
