# CmpHiveCacheEntryLockAcquire

- RVA: `0x007F5CD8`–`0x007F5D35` (길이 `93` bytes)
- VA: `0x00000001407F5CD8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `26`개 명령, `93/93` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007F5D02` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x007F5D1B` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)

### Direct callers
- [CmpHiveCacheClaimHiveEntry](CmpHiveCacheClaimHiveEntry_function_007F5970.md) at `0x007F59B5`
- [CmpHiveCacheClaimHiveEntry](CmpHiveCacheClaimHiveEntry_function_007F5970.md) at `0x007F5A2C`
- [CmpHiveCacheCreateHiveEntry](CmpHiveCacheCreateHiveEntry_function_007F5A68.md) at `0x007F5AA8`
- [CmpHiveCachePnpNotificationCallback](CmpHiveCachePnpNotificationCallback_function_007F5D80.md) at `0x007F5DFF`
- [CmpHiveCachePopulateHiveEntry](CmpHiveCachePopulateHiveEntry_function_007F5EB4.md) at `0x007F5F74`
- [CmpHiveCachePopulateHiveEntryThread](CmpHiveCachePopulateHiveEntryThread_function_007F5FD0.md) at `0x007F6058`
- [CmpHiveCachePopulateHiveEntryThread](CmpHiveCachePopulateHiveEntryThread_function_007F5FD0.md) at `0x007F62F4`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x007F5D02` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x007F5D1B` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007F5CD8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
007F5CDD  57                              push rdi
007F5CDE  48 83 EC 20                     sub rsp, 0x20
007F5CE2  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007F5CEB  48 8D B9 30 01 00 00            lea rdi, [rcx + 0x130]
007F5CF2  45 33 C0                        xor r8d, r8d
007F5CF5  33 D2                           xor edx, edx
007F5CF7  48 8B CF                        mov rcx, rdi
007F5CFA  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
007F5D01  90                              nop
007F5D02  E8 29 A5 A1 FF                  call 0x140210230
007F5D07  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
007F5D0D  48 8B D8                        mov rbx, rax
007F5D10  73 0E                           jae 0x1407f5d20
007F5D12  4C 8B C7                        mov r8, rdi
007F5D15  48 8B D0                        mov rdx, rax
007F5D18  48 8B CF                        mov rcx, rdi
007F5D1B  E8 70 9F A1 FF                  call 0x14020fc90
007F5D20  48 85 DB                        test rbx, rbx
007F5D23  74 04                           je 0x1407f5d29
007F5D25  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
007F5D29  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
007F5D2E  48 83 C4 20                     add rsp, 0x20
007F5D32  5F                              pop rdi
007F5D33  C3                              ret
007F5D34  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpHiveCacheEntryLockAcquire(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 304, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = a1 + 304;
        a2 = result;
        a1 = a1 + 304;
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
int64_t CmpHiveCacheEntryLockAcquire(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 304, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1 + 304;
        Arg2 = result;
        Arg1 = Arg1 + 304;
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
| `Arg1` | `+ 0x130` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007F5CD8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007F5CD8[BB_007F5CD8]
  bb_007F5D12[BB_007F5D12]
  bb_007F5D20[BB_007F5D20]
  bb_007F5D25[BB_007F5D25]
  bb_007F5D29[BB_007F5D29]
  bb_007F5D34[BB_007F5D34]
  bb_007F5CD8 -->|branch| bb_007F5D20
  bb_007F5CD8 -->|fallthrough| bb_007F5D12
  bb_007F5D12 -->|flow| bb_007F5D20
  bb_007F5D20 -->|branch| bb_007F5D29
  bb_007F5D20 -->|fallthrough| bb_007F5D25
  bb_007F5D25 -->|flow| bb_007F5D29
```
