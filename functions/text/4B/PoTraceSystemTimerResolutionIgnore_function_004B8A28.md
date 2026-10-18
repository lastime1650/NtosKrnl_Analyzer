# PoTraceSystemTimerResolutionIgnore

- RVA: `0x004B8A28`–`0x004B8AE5` (길이 `189` bytes)
- VA: `0x00000001404B8A28`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BB024`
- 디코드: `41`개 명령, `189/189` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x004B8A4E` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x004B8A62` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x004B8ADB` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)

### Direct callers
- [ExUpdateTimerResolutionPolicy](../../page/9C/ExUpdateTimerResolutionPolicy_function_009C579C.md) at `0x009C57D3`

### Static image references
- `0x004B8A2E` → RVA `0x00E0A740` (`.data`; read)
- `0x004B8A40` → RVA `0x0001C7D0` (`.rdata`; read)
- `0x004B8A47` → RVA `0x00F0B408` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B8A28  40 53                           push rbx
004B8A2A  48 83 EC 70                     sub rsp, 0x70
004B8A2E  48 8B 05 0B 1D 95 00            mov rax, qword ptr [rip + 0x951d0b]
004B8A35  48 33 C4                        xor rax, rsp
004B8A38  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
004B8A3D  48 8B D9                        mov rbx, rcx
004B8A40  48 8D 15 89 3D B6 FF            lea rdx, [rip - 0x49c277]
004B8A47  48 8B 0D BA 29 A5 00            mov rcx, qword ptr [rip + 0xa529ba]
004B8A4E  E8 FD 99 ED FF                  call 0x140392450
004B8A53  45 33 C0                        xor r8d, r8d
004B8A56  84 C0                           test al, al
004B8A58  75 14                           jne 0x1404b8a6e
004B8A5A  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
004B8A5F  48 33 CC                        xor rcx, rsp
004B8A62  E8 D9 3B 1F 00                  call 0x1406ac640
004B8A67  48 83 C4 70                     add rsp, 0x70
004B8A6B  5B                              pop rbx
004B8A6C  C3                              ret
004B8A6D  CC                              int3
004B8A6E  8B 83 D0 01 00 00               mov eax, dword ptr [rbx + 0x1d0]
004B8A74  48 8D 15 55 3D B6 FF            lea rdx, [rip - 0x49c2ab]
004B8A7B  48 8B 0D 86 29 A5 00            mov rcx, qword ptr [rip + 0xa52986]
004B8A82  45 33 C9                        xor r9d, r9d
004B8A85  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
004B8A89  8B 83 FC 05 00 00               mov eax, dword ptr [rbx + 0x5fc]
004B8A8F  C1 E8 1A                        shr eax, 0x1a
004B8A92  83 E0 01                        and eax, 1
004B8A95  48 C7 44 24 50 04 00 00 00      mov qword ptr [rsp + 0x50], 4
004B8A9E  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
004B8AA2  48 8D 44 24 40                  lea rax, [rsp + 0x40]
004B8AA7  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
004B8AAC  48 8D 44 24 44                  lea rax, [rsp + 0x44]
004B8AB1  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
004B8AB6  48 8D 44 24 48                  lea rax, [rsp + 0x48]
004B8ABB  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
004B8AC0  C7 44 24 30 02 00 00 00         mov dword ptr [rsp + 0x30], 2
004B8AC8  4C 89 44 24 28                  mov qword ptr [rsp + 0x28], r8
004B8ACD  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
004B8AD2  48 C7 44 24 60 04 00 00 00      mov qword ptr [rsp + 0x60], 4
004B8ADB  E8 F0 65 DA FF                  call 0x14025f0d0
004B8AE0  E9 75 FF FF FF                  jmp 0x1404b8a5a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PoTraceSystemTimerResolutionIgnore(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned int v_stack_p44;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;

    v_rsp = (v_rsp) - (112);
    result = (*(unsigned __int64 *)(v_rip + 9772299)) ^ (v_rsp);
    v_stack_m10 = result;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 10824122), v_rip - 4833911, a3, a4);
    a3 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_004B8A6E;
loc_004B8A5A:
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, v_rip - 4833911, a3, a4);
    v_rsp = (v_rsp) + (112);
    return result;
loc_004B8A6E:
    a4 = 0;
    v_stack_p44 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 464)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 1532))) >> (26));
    result = (unsigned int)((result) & (1));
    v_stack_p50 = 4;
    v_stack_p40 = (unsigned int)(result);
    v_stack_p48 = v_stack_p40;
    v_stack_p58 = v_stack_p44;
    v_stack_p38 = v_stack_p48;
    v_stack_p30 = 2;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    v_stack_p60 = 4;
    result = EtwWriteEx(*(unsigned __int64 *)(v_rip + 10824070), v_rip - 4833963, a3, a4);
    goto loc_004B8A5A;
}
```

## 5. (Beta) C Style

```c
int64_t PoTraceSystemTimerResolutionIgnore(void *Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint32_t v_stack_p44;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;

    local_rsp = (local_rsp) - (112);
    result = (*(uint64_t *)(v_rip + 0x951D0B)) ^ (local_rsp);
    v_stack_m10 = result;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0xA529BA), v_rip - 4833911, Arg3, Arg4);
    Arg3 = 0;
    if ((uint8_t)(result) != 0) goto loc_004B8A6E;
loc_004B8A5A:
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_rip - 4833911, Arg3, Arg4);
    local_rsp = (local_rsp) + (112);
    return result;
loc_004B8A6E:
    Arg4 = 0;
    v_stack_p44 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1D0)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x5FC))) >> (26));
    result = (uint32_t)((result) & (1));
    v_stack_p50 = 4;
    v_stack_p40 = (uint32_t)(result);
    v_stack_p48 = v_stack_p40;
    v_stack_p58 = v_stack_p44;
    v_stack_p38 = v_stack_p48;
    v_stack_p30 = 2;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    v_stack_p60 = 4;
    result = EtwWriteEx(*(uint64_t *)(v_rip + 0xA52986), v_rip - 4833963, Arg3, Arg4);
    goto loc_004B8A5A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1D0` | `32` | `R` |
| `Arg1` | `+ 0x5FC` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B8A28&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004B8A28[BB_004B8A28]
  bb_004B8A5A[BB_004B8A5A]
  bb_004B8A6D[BB_004B8A6D]
  bb_004B8A6E[BB_004B8A6E]
  bb_004B8A28 -->|branch| bb_004B8A6E
  bb_004B8A28 -->|fallthrough| bb_004B8A5A
  bb_004B8A6D -->|flow| bb_004B8A6E
  bb_004B8A6E -->|branch| bb_004B8A5A
```
