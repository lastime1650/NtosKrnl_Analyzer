# ObpPreInterceptHandleDuplicate

- RVA: `0x008C69E4`–`0x008C6AB2` (길이 `206` bytes)
- VA: `0x00000001408C69E4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00083BEC`
- 디코드: `59`개 명령, `206/206` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x008C6A82` → [ObpCallPreOperationCallbacks](ObpCallPreOperationCallbacks_function_008C6570.md) (function, `0x008C6570`)

### Direct callers
- [ObCompleteObjectDuplication](../89/ObCompleteObjectDuplication_function_0089387C.md) at `0x00893A95`

### Static image references
- `0x008C6A1F` → RVA `0x00FC7800` (`ALMOSTRO`; read)
- `0x008C6A2C` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008C69E4  48 8B C4                        mov rax, rsp
008C69E7  48 89 58 08                     mov qword ptr [rax + 8], rbx
008C69EB  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
008C69EF  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
008C69F3  4C 89 70 20                     mov qword ptr [rax + 0x20], r14
008C69F7  55                              push rbp
008C69F8  48 8B EC                        mov rbp, rsp
008C69FB  48 83 EC 60                     sub rsp, 0x60
008C69FF  44 0F B6 F2                     movzx r14d, dl
008C6A03  48 8D 41 D0                     lea rax, [rcx - 0x30]
008C6A07  48 C1 E8 08                     shr rax, 8
008C6A0B  48 8B D9                        mov rbx, rcx
008C6A0E  44 0F B6 D8                     movzx r11d, al
008C6A12  49 8B F8                        mov rdi, r8
008C6A15  0F B6 41 E8                     movzx eax, byte ptr [rcx - 0x18]
008C6A19  41 8B D6                        mov edx, r14d
008C6A1C  45 8B 00                        mov r8d, dword ptr [r8]
008C6A1F  48 8D 0D DA 0D 70 00            lea rcx, [rip + 0x700dda]
008C6A26  4C 33 D8                        xor r11, rax
008C6A29  83 E2 01                        and edx, 1
008C6A2C  0F B6 05 19 04 70 00            movzx eax, byte ptr [rip + 0x700419]
008C6A33  4C 33 D8                        xor r11, rax
008C6A36  48 8D 45 C0                     lea rax, [rbp - 0x40]
008C6A3A  4A 8B 0C D9                     mov rcx, qword ptr [rcx + r11*8]
008C6A3E  8B 71 60                        mov esi, dword ptr [rcx + 0x60]
008C6A41  48 83 65 F0 00                  and qword ptr [rbp - 0x10], 0
008C6A46  41 23 F0                        and esi, r8d
008C6A49  48 89 45 F8                     mov qword ptr [rbp - 8], rax
008C6A4D  33 C0                           xor eax, eax
008C6A4F  83 E0 FE                        and eax, 0xfffffffe
008C6A52  44 89 45 C4                     mov dword ptr [rbp - 0x3c], r8d
008C6A56  0B D0                           or edx, eax
008C6A58  44 89 45 C0                     mov dword ptr [rbp - 0x40], r8d
008C6A5C  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
008C6A60  4C 8B 45 38                     mov r8, qword ptr [rbp + 0x38]
008C6A64  89 55 DC                        mov dword ptr [rbp - 0x24], edx
008C6A67  48 8D 55 D8                     lea rdx, [rbp - 0x28]
008C6A6B  C7 45 D8 02 00 00 00            mov dword ptr [rbp - 0x28], 2
008C6A72  48 89 5D E0                     mov qword ptr [rbp - 0x20], rbx
008C6A76  48 89 4D E8                     mov qword ptr [rbp - 0x18], rcx
008C6A7A  4C 89 4D C8                     mov qword ptr [rbp - 0x38], r9
008C6A7E  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
008C6A82  E8 E9 FA FF FF                  call 0x1408c6570
008C6A87  85 C0                           test eax, eax
008C6A89  78 0C                           js 0x1408c6a97
008C6A8B  45 84 F6                        test r14b, r14b
008C6A8E  75 07                           jne 0x1408c6a97
008C6A90  8B 4D C0                        mov ecx, dword ptr [rbp - 0x40]
008C6A93  0B CE                           or ecx, esi
008C6A95  21 0F                           and dword ptr [rdi], ecx
008C6A97  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
008C6A9C  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
008C6AA0  49 8B 73 18                     mov rsi, qword ptr [r11 + 0x18]
008C6AA4  49 8B 7B 20                     mov rdi, qword ptr [r11 + 0x20]
008C6AA8  4D 8B 73 28                     mov r14, qword ptr [r11 + 0x28]
008C6AAC  49 8B E3                        mov rsp, r11
008C6AAF  5D                              pop rbp
008C6AB0  C3                              ret
008C6AB1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObpPreInterceptHandleDuplicate(__int64 a1, unsigned __int8 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m44;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 32) = v_r14;
    v_rsp = (v_rsp) - (96);
    result = (a1 - 48) >> (8);
    v_r11 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(a1 - 24));
    a2 = (unsigned int)(((unsigned int)(a2)) & (1));
    v_r11 = (v_r11) ^ (*(unsigned __int8 *)(v_rip + 7341081));
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7343578 + v_r11 * 8) + 96))) & ((unsigned int)((unsigned int)(*(unsigned int *)(a3)))));
    v_stack_m10 = v_stack_m48;
    result = 0;
    result = (unsigned int)((result) & (0xFFFFFFFEULL));
    v_stack_m44 = (unsigned int)((unsigned int)(*(unsigned int *)(a3)));
    a2 = (unsigned int)((a2) | ((unsigned int)(result)));
    v_stack_m48 = (unsigned int)((unsigned int)(*(unsigned int *)(a3)));
    v_stack_m2C = a2;
    v_stack_m30 = 2;
    v_stack_m28 = a1;
    v_stack_m20 = *(unsigned __int64 *)(v_rip + 7343578 + v_r11 * 8);
    v_stack_m40 = a4;
    v_stack_m38 = a5;
    result = ObpCallPreOperationCallbacks(*(unsigned __int64 *)(v_rip + 7343578 + v_r11 * 8), v_stack_m30, a6, a4);
    if (sign_flag) goto loc_008C6A97;
    if (a2 == 0) {
        a1 = v_stack_m48;
        a1 = (unsigned int)((a1) | ((unsigned int)(v_rsi)));
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ObpPreInterceptHandleDuplicate(void *Arg1, uint8_t Arg2, void *Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r11;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint32_t v_stack_m44;
    uint64_t v_stack_m48;
    uint64_t v_stack_m8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    *(uint64_t *)(local_rsp + 0x20) = local_r14;
    local_rsp = (local_rsp) - (96);
    result = (Arg1 - 48) >> (8);
    local_r11 = ((uint8_t)(result)) ^ (*(uint8_t *)(arg1 - 0x18));
    Arg2 = (uint32_t)(((uint32_t)(Arg2)) & (1));
    local_r11 = (local_r11) ^ (*(uint8_t *)(v_rip + 0x700419));
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x700DDA + local_r11 * 8) + 0x60))) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg3)))));
    v_stack_m10 = v_stack_m48;
    result = 0;
    result = (uint32_t)((result) & (0xFFFFFFFEULL));
    v_stack_m44 = (uint32_t)((uint32_t)(*(uint32_t *)(arg3)));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(result)));
    v_stack_m48 = (uint32_t)((uint32_t)(*(uint32_t *)(arg3)));
    v_stack_m2C = Arg2;
    v_stack_m30 = 2;
    v_stack_m28 = Arg1;
    v_stack_m20 = *(uint64_t *)(v_rip + 0x700DDA + local_r11 * 8);
    v_stack_m40 = Arg4;
    v_stack_m38 = Arg5;
    result = ObpCallPreOperationCallbacks(*(uint64_t *)(v_rip + 0x700DDA + local_r11 * 8), v_stack_m30, Arg6, Arg4);
    if (sign_flag) goto loc_008C6A97;
    if (Arg2 == 0) {
        Arg1 = v_stack_m48;
        Arg1 = (uint32_t)((Arg1) | ((uint32_t)(local_rsi)));
    }
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x30` | `64` | `R` |
| `Arg1` | `- 0x18` | `8` | `R` |
| `Arg3` | `+ 0x0` | `32` | `R` |
| `Arg3` | `+ 0x0` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008C69E4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008C69E4[BB_008C69E4]
  bb_008C6A8B[BB_008C6A8B]
  bb_008C6A90[BB_008C6A90]
  bb_008C6A97[BB_008C6A97]
  bb_008C6AB1[BB_008C6AB1]
  bb_008C69E4 -->|branch| bb_008C6A97
  bb_008C69E4 -->|fallthrough| bb_008C6A8B
  bb_008C6A8B -->|branch| bb_008C6A97
  bb_008C6A8B -->|fallthrough| bb_008C6A90
  bb_008C6A90 -->|flow| bb_008C6A97
```
