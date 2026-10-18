# PiDqQueryLock

- RVA: `0x008DDA0C`–`0x008DDA66` (길이 `90` bytes)
- VA: `0x00000001408DDA0C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `26`개 명령, `90/90` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008DDA33` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008DDA4C` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)

### Direct callers
- [PiDqIrpCancel](../../text/5A/PiDqIrpCancel_function_005A7CA0.md) at `0x005A7CD4`
- [PiDqIrpQueryGetResult](PiDqIrpQueryGetResult_function_008DBF28.md) at `0x008DBF8D`
- [PiDqIrpQueryGetResult](PiDqIrpQueryGetResult_function_008DBF28.md) at `0x008DC044`
- [PiDqIrpQueryGetResult](PiDqIrpQueryGetResult_function_008DBF28.md) at `0x008DC0AB`
- [PiDqIrpQueryGetResult](PiDqIrpQueryGetResult_function_008DBF28.md) at `0x008DC126`
- [PiDqDispatch](PiDqDispatch_function_008DC8A0.md) at `0x008DC8FF`
- [PiDqDispatch](PiDqDispatch_function_008DC8A0.md) at `0x008DC934`
- [PiDqIrpQueryCreate](PiDqIrpQueryCreate_function_008DCC04.md) at `0x008DCCAA`
- [PiDqIrpQueryCreate](PiDqIrpQueryCreate_function_008DCC04.md) at `0x008DCE21`
- [PiDqObjectManagerEnumerateAndRegisterQuery](PiDqObjectManagerEnumerateAndRegisterQuery_function_008DCF74.md) at `0x008DCFF0`
- [PiDqObjectManagerEnumerateAndRegisterQuery](PiDqObjectManagerEnumerateAndRegisterQuery_function_008DCF74.md) at `0x008DD28A`
- [PiDqQuerySerializeActionQueue](PiDqQuerySerializeActionQueue_function_008DD340.md) at `0x008DD383`
- [PiDqQuerySerializeActionQueue](PiDqQuerySerializeActionQueue_function_008DD340.md) at `0x008DD435`
- [PiDqQuerySerializeActionQueue](PiDqQuerySerializeActionQueue_function_008DD340.md) at `0x008DD500`
- [PiDqQuerySerializeActionQueue](PiDqQuerySerializeActionQueue_function_008DD340.md) at `0x008DD5EA`
- [PiDqObjectManagerServiceActionQueue](PiDqObjectManagerServiceActionQueue_function_008DD640.md) at `0x008DD909`
- [PiDqObjectManagerServiceActionQueue](PiDqObjectManagerServiceActionQueue_function_008DD640.md) at `0x008DD930`
- [PiDqQueryApplyObjectEvent](PiDqQueryApplyObjectEvent_function_008DDACC.md) at `0x008DDB23`
- [PiDqQueryApplyObjectEvent](PiDqQueryApplyObjectEvent_function_008DDACC.md) at `0x008DDD24`
- [PiDqQueryApplyObjectEvent](PiDqQueryApplyObjectEvent_function_008DDACC.md) at `0x008DDD8F`
- [PiDqQueryApplyObjectEvent](PiDqQueryApplyObjectEvent_function_008DDACC.md) at `0x008DDDBA`
- [PiDqQueryApplyObjectEvent](PiDqQueryApplyObjectEvent_function_008DDACC.md) at `0x008DE03A`
- [PiDqQueryApplyObjectEvent](PiDqQueryApplyObjectEvent_function_008DDACC.md) at `0x008DE06F`
- [PiDqQueryApplyObjectEvent](PiDqQueryApplyObjectEvent_function_008DDACC.md) at `0x008DE100`
- [sub_00B1CDEE](../B1/Unknown_function_00B1CDEE.md) at `0x00B1CDF1`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x008DDA33` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008DDA4C` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008DDA0C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
008DDA11  57                              push rdi
008DDA12  48 83 EC 20                     sub rsp, 0x20
008DDA16  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008DDA1F  48 8D 79 40                     lea rdi, [rcx + 0x40]
008DDA23  45 33 C0                        xor r8d, r8d
008DDA26  33 D2                           xor edx, edx
008DDA28  48 8B CF                        mov rcx, rdi
008DDA2B  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008DDA32  90                              nop
008DDA33  E8 F8 27 93 FF                  call 0x140210230
008DDA38  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
008DDA3E  48 8B D8                        mov rbx, rax
008DDA41  73 0E                           jae 0x1408dda51
008DDA43  4C 8B C7                        mov r8, rdi
008DDA46  48 8B D0                        mov rdx, rax
008DDA49  48 8B CF                        mov rcx, rdi
008DDA4C  E8 3F 22 93 FF                  call 0x14020fc90
008DDA51  48 85 DB                        test rbx, rbx
008DDA54  74 04                           je 0x1408dda5a
008DDA56  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
008DDA5A  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
008DDA5F  48 83 C4 20                     add rsp, 0x20
008DDA63  5F                              pop rdi
008DDA64  C3                              ret
008DDA65  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDqQueryLock(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 64, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = a1 + 64;
        a2 = result;
        a1 = a1 + 64;
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
int64_t PiDqQueryLock(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 64, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1 + 64;
        Arg2 = result;
        Arg1 = Arg1 + 64;
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
| `Arg1` | `+ 0x40` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008DDA0C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008DDA0C[BB_008DDA0C]
  bb_008DDA43[BB_008DDA43]
  bb_008DDA51[BB_008DDA51]
  bb_008DDA56[BB_008DDA56]
  bb_008DDA5A[BB_008DDA5A]
  bb_008DDA65[BB_008DDA65]
  bb_008DDA0C -->|branch| bb_008DDA51
  bb_008DDA0C -->|fallthrough| bb_008DDA43
  bb_008DDA43 -->|flow| bb_008DDA51
  bb_008DDA51 -->|branch| bb_008DDA5A
  bb_008DDA51 -->|fallthrough| bb_008DDA56
  bb_008DDA56 -->|flow| bb_008DDA5A
```
