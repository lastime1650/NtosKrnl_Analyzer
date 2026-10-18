# ExpLockHandleTableExclusive

- RVA: `0x00458B08`–`0x00458B59` (길이 `81` bytes)
- VA: `0x0000000140458B08`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `25`개 명령, `81/81` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00458B26` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00458B3F` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)

### Direct callers
- [ExDisableHandleTracing](../65/ExDisableHandleTracing_function_00655CBC.md) at `0x00655CDA`
- [PspApplyMitigationOptions](../../page/A6/PspApplyMitigationOptions_function_00A699AC.md) at `0x00A6A40A`
- [ExEnableRaiseUMExceptionOnInvalidHandleClose](../../page/A6/ExEnableRaiseUMExceptionOnInvalidHandleClose_function_00A6A868.md) at `0x00A6A888`
- [ExEnableHandleExceptions](../../page/A7/ExEnableHandleExceptions_function_00A7580C.md) at `0x00A75832`
- [ExEnableHandleTracing](../../page/AD/ExEnableHandleTracing_function_00AD2C8C.md) at `0x00AD2DEE`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00458B08  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00458B0D  57                              push rdi
00458B0E  48 83 EC 20                     sub rsp, 0x20
00458B12  66 FF 8A E4 01 00 00            dec word ptr [rdx + 0x1e4]
00458B19  48 8D 79 38                     lea rdi, [rcx + 0x38]
00458B1D  48 8B CF                        mov rcx, rdi
00458B20  45 33 C0                        xor r8d, r8d
00458B23  33 D2                           xor edx, edx
00458B25  90                              nop
00458B26  E8 05 77 DB FF                  call 0x140210230
00458B2B  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
00458B31  48 8B D8                        mov rbx, rax
00458B34  73 0E                           jae 0x140458b44
00458B36  4C 8B C7                        mov r8, rdi
00458B39  48 8B D0                        mov rdx, rax
00458B3C  48 8B CF                        mov rcx, rdi
00458B3F  E8 4C 71 DB FF                  call 0x14020fc90
00458B44  48 85 DB                        test rbx, rbx
00458B47  74 04                           je 0x140458b4d
00458B49  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
00458B4D  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00458B52  48 83 C4 20                     add rsp, 0x20
00458B56  5F                              pop rdi
00458B57  C3                              ret
00458B58  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpLockHandleTableExclusive(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 56, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = a1 + 56;
        a2 = result;
        a1 = a1 + 56;
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
int64_t ExpLockHandleTableExclusive(void *Arg1, void *Arg2, int32_t Arg3)
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
    result = KeAbPreAcquire(Arg1 + 56, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1 + 56;
        Arg2 = result;
        Arg1 = Arg1 + 56;
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
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg2` | `+ 0x1E4` | `16` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00458B08&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00458B08[BB_00458B08]
  bb_00458B36[BB_00458B36]
  bb_00458B44[BB_00458B44]
  bb_00458B49[BB_00458B49]
  bb_00458B4D[BB_00458B4D]
  bb_00458B58[BB_00458B58]
  bb_00458B08 -->|branch| bb_00458B44
  bb_00458B08 -->|fallthrough| bb_00458B36
  bb_00458B36 -->|flow| bb_00458B44
  bb_00458B44 -->|branch| bb_00458B4D
  bb_00458B44 -->|fallthrough| bb_00458B49
  bb_00458B49 -->|flow| bb_00458B4D
```
