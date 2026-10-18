# PpmEventHiddenProcessorPerformance

- RVA: `0x0076A424`–`0x0076A522` (길이 `254` bytes)
- VA: `0x000000014076A424`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CD20C`
- 디코드: `57`개 명령, `254/254` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0076A46E` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x0076A4FF` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x0076A50B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PpmEventTraceProcessorPerformance](../A5/PpmEventTraceProcessorPerformance_function_00A5237C.md) at `0x00A52769`

### Static image references
- `0x0076A442` → RVA `0x00E0A740` (`.data`; read)
- `0x0076A450` → RVA `0x00E67A39` (`.data`; read)
- `0x0076A460` → RVA `0x00F083E8` (`.data`; read)
- `0x0076A467` → RVA `0x00022758` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0076A46E` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x0076A4FF` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x0076A50B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0076A424  48 8B C4                        mov rax, rsp
0076A427  48 89 58 08                     mov qword ptr [rax + 8], rbx
0076A42B  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
0076A42F  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
0076A433  89 50 10                        mov dword ptr [rax + 0x10], edx
0076A436  55                              push rbp
0076A437  48 8D 68 A1                     lea rbp, [rax - 0x5f]
0076A43B  48 81 EC A0 00 00 00            sub rsp, 0xa0
0076A442  48 8B 05 F7 02 6A 00            mov rax, qword ptr [rip + 0x6a02f7]
0076A449  48 33 C4                        xor rax, rsp
0076A44C  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
0076A450  80 3D E2 D5 6F 00 00            cmp byte ptr [rip + 0x6fd5e2], 0
0076A457  48 8B D9                        mov rbx, rcx
0076A45A  0F 84 A4 00 00 00               je 0x14076a504
0076A460  48 8B 0D 81 DF 79 00            mov rcx, qword ptr [rip + 0x79df81]
0076A467  48 8D 15 EA 82 8B FF            lea rdx, [rip - 0x747d16]
0076A46E  E8 DD 7F C2 FF                  call 0x140392450
0076A473  84 C0                           test al, al
0076A475  0F 84 89 00 00 00               je 0x14076a504
0076A47B  0F B6 83 D0 00 00 00            movzx eax, byte ptr [rbx + 0xd0]
0076A482  48 8D 15 CF 82 8B FF            lea rdx, [rip - 0x747d31]
0076A489  83 65 03 00                     and dword ptr [rbp + 3], 0
0076A48D  B9 04 00 00 00                  mov ecx, 4
0076A492  83 65 13 00                     and dword ptr [rbp + 0x13], 0
0076A496  45 33 C0                        xor r8d, r8d
0076A499  83 65 23 00                     and dword ptr [rbp + 0x23], 0
0076A49D  83 65 33 00                     and dword ptr [rbp + 0x33], 0
0076A4A1  83 65 43 00                     and dword ptr [rbp + 0x43], 0
0076A4A5  44 8D 49 01                     lea r9d, [rcx + 1]
0076A4A9  66 89 45 E7                     mov word ptr [rbp - 0x19], ax
0076A4AD  48 8D 45 E7                     lea rax, [rbp - 0x19]
0076A4B1  48 89 45 F7                     mov qword ptr [rbp - 9], rax
0076A4B5  48 8D 83 D1 00 00 00            lea rax, [rbx + 0xd1]
0076A4BC  48 89 45 07                     mov qword ptr [rbp + 7], rax
0076A4C0  48 8D 45 6F                     lea rax, [rbp + 0x6f]
0076A4C4  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
0076A4C8  48 8D 45 77                     lea rax, [rbp + 0x77]
0076A4CC  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
0076A4D0  48 8D 45 7F                     lea rax, [rbp + 0x7f]
0076A4D4  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
0076A4D8  48 8D 45 F7                     lea rax, [rbp - 9]
0076A4DC  89 4D 1F                        mov dword ptr [rbp + 0x1f], ecx
0076A4DF  89 4D 2F                        mov dword ptr [rbp + 0x2f], ecx
0076A4E2  89 4D 3F                        mov dword ptr [rbp + 0x3f], ecx
0076A4E5  48 8B 0D FC DE 79 00            mov rcx, qword ptr [rip + 0x79defc]
0076A4EC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0076A4F1  C7 45 FF 02 00 00 00            mov dword ptr [rbp - 1], 2
0076A4F8  C7 45 0F 01 00 00 00            mov dword ptr [rbp + 0xf], 1
0076A4FF  E8 1C 22 CB FF                  call 0x14041c720
0076A504  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
0076A508  48 33 CC                        xor rcx, rsp
0076A50B  E8 30 21 F4 FF                  call 0x1406ac640
0076A510  48 8B 9C 24 B0 00 00 00         mov rbx, qword ptr [rsp + 0xb0]
0076A518  48 81 C4 A0 00 00 00            add rsp, 0xa0
0076A51F  5D                              pop rbp
0076A520  C3                              ret
0076A521  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmEventHiddenProcessorPerformance(__int64 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned int *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 6947575)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 71) = result;
    if ((*(unsigned __int8 *)(v_rip + 7329250)) == 0) goto loc_0076A504;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 7987073), v_rip - 7634198, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = *(unsigned __int8 *)(a1 + 208);
        a2 = v_rip - 7634225;
        a1 = 4;
        a3 = 0;
        a4 = a1 + 1;
        *(unsigned __int16 *)(v_rsp - 95 - 25) = (unsigned __int16)(result);
        result = v_rsp - 95 - 25;
        *(unsigned __int64 *)(v_rsp - 95 - 9) = result;
        result = a1 + 209;
        *(unsigned __int64 *)(v_rsp - 95 + 7) = result;
        result = v_rsp - 95 + 111;
        *(unsigned __int64 *)(v_rsp - 95 + 23) = result;
        result = v_rsp - 95 + 119;
        *(unsigned __int64 *)(v_rsp - 95 + 39) = result;
        result = v_rsp - 95 + 127;
        *(unsigned __int64 *)(v_rsp - 95 + 55) = result;
        result = v_rsp - 95 - 9;
        *(unsigned int *)(v_rsp - 95 + 31) = (unsigned int)(a1);
        *(unsigned int *)(v_rsp - 95 + 47) = (unsigned int)(a1);
        *(unsigned int *)(v_rsp - 95 + 63) = (unsigned int)(a1);
        a1 = *(unsigned __int64 *)(v_rip + 7986940);
        v_stack_m88 = result;
        *(unsigned int *)(v_rsp - 95 - 1) = 2;
        *(unsigned int *)(v_rsp - 95 + 15) = 1;
        result = EtwWrite(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 71)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (160);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpmEventHiddenProcessorPerformance(void *Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m88;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint32_t *)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x6A02F7)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x47) = result;
    if ((*(uint8_t *)(v_rip + 0x6FD5E2)) == 0) goto loc_0076A504;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x79DF81), v_rip - 7634198, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = *(uint8_t *)(arg1 + 0xD0);
        Arg2 = v_rip - 7634225;
        Arg1 = 4;
        Arg3 = 0;
        Arg4 = Arg1 + 1;
        *(uint16_t *)(local_rsp - 0x5F - 0x19) = (uint16_t)(result);
        result = local_rsp - 95 - 25;
        *(uint64_t *)(local_rsp - 0x5F - 0x9) = result;
        result = Arg1 + 209;
        *(uint64_t *)(local_rsp - 0x5F + 0x7) = result;
        result = local_rsp - 95 + 111;
        *(uint64_t *)(local_rsp - 0x5F + 0x17) = result;
        result = local_rsp - 95 + 119;
        *(uint64_t *)(local_rsp - 0x5F + 0x27) = result;
        result = local_rsp - 95 + 127;
        *(uint64_t *)(local_rsp - 0x5F + 0x37) = result;
        result = local_rsp - 95 - 9;
        *(uint32_t *)(local_rsp - 0x5F + 0x1F) = (uint32_t)(Arg1);
        *(uint32_t *)(local_rsp - 0x5F + 0x2F) = (uint32_t)(Arg1);
        *(uint32_t *)(local_rsp - 0x5F + 0x3F) = (uint32_t)(Arg1);
        Arg1 = *(uint64_t *)(v_rip + 0x79DEFC);
        v_stack_m88 = result;
        *(uint32_t *)(local_rsp - 0x5F - 0x1) = 2;
        *(uint32_t *)(local_rsp - 0x5F + 0xF) = 1;
        result = EtwWrite(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x47)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (160);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xD0` | `8` | `R` |
| `Arg1` | `+ 0xD1` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0076A424&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0076A424[BB_0076A424]
  bb_0076A460[BB_0076A460]
  bb_0076A47B[BB_0076A47B]
  bb_0076A504[BB_0076A504]
  bb_0076A521[BB_0076A521]
  bb_0076A424 -->|branch| bb_0076A504
  bb_0076A424 -->|fallthrough| bb_0076A460
  bb_0076A460 -->|branch| bb_0076A504
  bb_0076A460 -->|fallthrough| bb_0076A47B
  bb_0076A47B -->|flow| bb_0076A504
```
