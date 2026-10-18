# CmpTraceHiveLoadStart

- RVA: `0x00876F38`–`0x00876FF6` (길이 `190` bytes)
- VA: `0x0000000140876F38`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006CB28`
- 디코드: `45`개 명령, `190/190` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00876F74` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00876F86` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00876FEF` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)

### Direct callers
- [CmLoadDifferencingKey](CmLoadDifferencingKey_function_00875670.md) at `0x00875BCF`

### Static image references
- `0x00876F4C` → RVA `0x00E0A740` (`.data`; read)
- `0x00876F5A` → RVA `0x00010898` (`.rdata`; read)
- `0x00876F68` → RVA `0x00FD8018` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00876F74` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00876F86` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00876FEF` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00876F38  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00876F3D  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
00876F41  55                              push rbp
00876F42  48 8B EC                        mov rbp, rsp
00876F45  48 81 EC 80 00 00 00            sub rsp, 0x80
00876F4C  48 8B 05 ED 37 59 00            mov rax, qword ptr [rip + 0x5937ed]
00876F53  48 33 C4                        xor rax, rsp
00876F56  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00876F5A  0F 10 05 37 99 79 FF            movups xmm0, xmmword ptr [rip - 0x8666c9]
00876F61  48 8B D9                        mov rbx, rcx
00876F64  48 8D 55 B8                     lea rdx, [rbp - 0x48]
00876F68  48 8B 0D A9 10 76 00            mov rcx, qword ptr [rip + 0x7610a9]
00876F6F  F3 0F 7F 45 B8                  movdqu xmmword ptr [rbp - 0x48], xmm0
00876F74  E8 D7 B4 B1 FF                  call 0x140392450
00876F79  33 C9                           xor ecx, ecx
00876F7B  84 C0                           test al, al
00876F7D  75 1E                           jne 0x140876f9d
00876F7F  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
00876F83  48 33 CC                        xor rcx, rsp
00876F86  E8 B5 56 E3 FF                  call 0x1406ac640
00876F8B  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
00876F93  48 81 C4 80 00 00 00            add rsp, 0x80
00876F9A  5D                              pop rbp
00876F9B  C3                              ret
00876F9C  CC                              int3
00876F9D  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00876FA1  48 8D 55 B8                     lea rdx, [rbp - 0x48]
00876FA5  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00876FA9  41 B9 03 00 00 00               mov r9d, 3
00876FAF  0F B7 03                        movzx eax, word ptr [rbx]
00876FB2  45 33 C0                        xor r8d, r8d
00876FB5  89 45 D0                        mov dword ptr [rbp - 0x30], eax
00876FB8  48 8D 45 B0                     lea rax, [rbp - 0x50]
00876FBC  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
00876FC0  48 8D 45 18                     lea rax, [rbp + 0x18]
00876FC4  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00876FC8  48 8D 45 C8                     lea rax, [rbp - 0x38]
00876FCC  66 89 4D B0                     mov word ptr [rbp - 0x50], cx
00876FD0  89 4D D4                        mov dword ptr [rbp - 0x2c], ecx
00876FD3  48 8B 0D 3E 10 76 00            mov rcx, qword ptr [rip + 0x76103e]
00876FDA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00876FDF  48 C7 45 E0 02 00 00 00         mov qword ptr [rbp - 0x20], 2
00876FE7  48 C7 45 F0 04 00 00 00         mov qword ptr [rbp - 0x10], 4
00876FEF  E8 2C 57 BA FF                  call 0x14041c720
00876FF4  EB 89                           jmp 0x140876f7f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpTraceHiveLoadStart(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned int v_stack_m34;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (128);
    result = (*(unsigned __int64 *)(v_rip + 5847021)) ^ (v_rsp);
    v_stack_m10 = result;
    v_stack_m50 = v_xmm0;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 7737513), v_stack_m50, a3, a4);
    a1 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_00876F9D;
loc_00876F7F:
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m50, a3, a4);
    v_rsp = (v_rsp) + (128);
    return result;
loc_00876F9D:
    v_stack_m40 = *(unsigned __int64 *)(v_stack_p8 + 8);
    a3 = 0;
    v_stack_m38 = (unsigned int)(*(unsigned __int16 *)(v_stack_p8));
    v_stack_m30 = v_stack_m58;
    v_stack_m20 = v_stack_p10;
    v_stack_m58 = (unsigned __int16)(a1);
    v_stack_m34 = (unsigned int)(a1);
    v_stack_p20 = v_stack_m40;
    v_stack_m28 = 2;
    v_stack_m18 = 4;
    result = EtwWrite(*(unsigned __int64 *)(v_rip + 7737406), v_stack_m50, a3, 3);
    goto loc_00876F7F;
}
```

## 5. (Beta) C Style

```c
int64_t CmpTraceHiveLoadStart(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint32_t v_stack_m34;
    uint32_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_p10;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (128);
    result = (*(uint64_t *)(v_rip + 0x5937ED)) ^ (local_rsp);
    v_stack_m10 = result;
    v_stack_m50 = v_xmm0;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x7610A9), v_stack_m50, Arg3, a4);
    Arg1 = 0;
    if ((uint8_t)(result) != 0) goto loc_00876F9D;
loc_00876F7F:
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m50, Arg3, a4);
    local_rsp = (local_rsp) + (128);
    return result;
loc_00876F9D:
    v_stack_m40 = *(uint64_t *)(v_stack_p8 + 0x8);
    Arg3 = 0;
    v_stack_m38 = (uint32_t)(*(uint16_t *)(v_stack_p8));
    v_stack_m30 = v_stack_m58;
    v_stack_m20 = v_stack_p10;
    v_stack_m58 = (uint16_t)(Arg1);
    v_stack_m34 = (uint32_t)(Arg1);
    v_stack_p20 = v_stack_m40;
    v_stack_m28 = 2;
    v_stack_m18 = 4;
    result = EtwWrite(*(uint64_t *)(v_rip + 0x76103E), v_stack_m50, Arg3, 3);
    goto loc_00876F7F;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00876F38&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00876F38[BB_00876F38]
  bb_00876F7F[BB_00876F7F]
  bb_00876F9C[BB_00876F9C]
  bb_00876F9D[BB_00876F9D]
  bb_00876F38 -->|branch| bb_00876F9D
  bb_00876F38 -->|fallthrough| bb_00876F7F
  bb_00876F9C -->|flow| bb_00876F9D
  bb_00876F9D -->|branch| bb_00876F7F
```
