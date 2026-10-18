# sub_00A34F4C

- RVA: `0x00A34F4C`–`0x00A3503A` (길이 `238` bytes)
- VA: `0x0000000140A34F4C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AD678`
- 디코드: `48`개 명령, `238/238` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00A35013` → [sub_0040C2C0](../../text/40/Unknown_function_0040C2C0.md) (function, `0x0040C2C0`)
- `0x00A35025` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00A35033` → [sub_0040C640](../../text/40/Unknown_function_0040C640.md) (function, `0x0040C640`)

### Direct callers
- [sub_00811EE0](../81/Unknown_function_00811EE0.md) at `0x0081206C`
- [sub_009A262C](../9A/Unknown_function_009A262C.md) at `0x009A270E`

### Static image references
- `0x00A34F53` → RVA `0x00E0A740` (`.data`; read)
- `0x00A34F6D` → RVA `0x000029F0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00A35013` → [sub_0040C2C0](../../text/40/Unknown_function_0040C2C0.md) (`PAGE` → `.text`)
  - `0x00A35025` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00A35033` → [sub_0040C640](../../text/40/Unknown_function_0040C640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A34F4C  48 81 EC 08 01 00 00            sub rsp, 0x108
00A34F53  48 8B 05 E6 57 3D 00            mov rax, qword ptr [rip + 0x3d57e6]
00A34F5A  48 33 C4                        xor rax, rsp
00A34F5D  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
00A34F65  4C 8B 94 24 40 01 00 00         mov r10, qword ptr [rsp + 0x140]
00A34F6D  48 8D 05 7C DA 5C FF            lea rax, [rip - 0xa32584]
00A34F74  4C 8B 9C 24 50 01 00 00         mov r11, qword ptr [rsp + 0x150]
00A34F7C  85 C9                           test ecx, ecx
00A34F7E  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00A34F83  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00A34F88  4C 89 5C 24 30                  mov qword ptr [rsp + 0x30], r11
00A34F8D  41 0F 10 02                     movups xmm0, xmmword ptr [r10]
00A34F91  41 0F 10 4A 10                  movups xmm1, xmmword ptr [r10 + 0x10]
00A34F96  0F 11 00                        movups xmmword ptr [rax], xmm0
00A34F99  41 0F 10 42 20                  movups xmm0, xmmword ptr [r10 + 0x20]
00A34F9E  0F 11 48 10                     movups xmmword ptr [rax + 0x10], xmm1
00A34FA2  41 0F 10 4A 30                  movups xmm1, xmmword ptr [r10 + 0x30]
00A34FA7  0F 11 40 20                     movups xmmword ptr [rax + 0x20], xmm0
00A34FAB  41 0F 10 42 40                  movups xmm0, xmmword ptr [r10 + 0x40]
00A34FB0  0F 11 48 30                     movups xmmword ptr [rax + 0x30], xmm1
00A34FB4  41 0F 10 4A 50                  movups xmm1, xmmword ptr [r10 + 0x50]
00A34FB9  0F 11 40 40                     movups xmmword ptr [rax + 0x40], xmm0
00A34FBD  41 0F 10 42 60                  movups xmm0, xmmword ptr [r10 + 0x60]
00A34FC2  0F 11 48 50                     movups xmmword ptr [rax + 0x50], xmm1
00A34FC6  41 0F 10 8A 80 00 00 00         movups xmm1, xmmword ptr [r10 + 0x80]
00A34FCE  0F 11 40 60                     movups xmmword ptr [rax + 0x60], xmm0
00A34FD2  41 0F 10 42 70                  movups xmm0, xmmword ptr [r10 + 0x70]
00A34FD7  0F 11 40 70                     movups xmmword ptr [rax + 0x70], xmm0
00A34FDB  41 0F 10 82 90 00 00 00         movups xmm0, xmmword ptr [r10 + 0x90]
00A34FE3  0F 11 88 80 00 00 00            movups xmmword ptr [rax + 0x80], xmm1
00A34FEA  0F 11 80 90 00 00 00            movups xmmword ptr [rax + 0x90], xmm0
00A34FF1  8B 84 24 38 01 00 00            mov eax, dword ptr [rsp + 0x138]
00A34FF8  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00A34FFC  48 8B 84 24 30 01 00 00         mov rax, qword ptr [rsp + 0x130]
00A35004  48 8B 08                        mov rcx, qword ptr [rax]
00A35007  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00A3500C  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00A35011  74 20                           je 0x140a35033
00A35013  E8 A8 72 9D FF                  call 0x14040c2c0
00A35018  33 C0                           xor eax, eax
00A3501A  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
00A35022  48 33 CC                        xor rcx, rsp
00A35025  E8 16 76 C7 FF                  call 0x1406ac640
00A3502A  48 81 C4 08 01 00 00            add rsp, 0x108
00A35031  C3                              ret
00A35032  CC                              int3
00A35033  E8 08 76 9D FF                  call 0x14040c640
00A35038  EB DE                           jmp 0x140a35018
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00A34F4C(int a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6, __int64 a7, __int64 a8, __int64 a9)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mE0;
    unsigned __int64 v_stack_mE8;

    v_rsp = (v_rsp) - (264);
    result = (*(unsigned __int64 *)(v_rip + 4020198)) ^ (v_rsp);
    v_stack_m18 = result;
    v_stack_mC8 = v_rip - 10691972;
    v_stack_mD8 = a9;
    *(unsigned __int64 *)(v_stack_mC0) = v_xmm0;
    *(unsigned __int64 *)(v_stack_mC0 + 16) = v_xmm1;
    *(unsigned __int64 *)(v_stack_mC0 + 32) = v_xmm0;
    *(unsigned __int64 *)(v_stack_mC0 + 48) = v_xmm1;
    *(unsigned __int64 *)(v_stack_mC0 + 64) = v_xmm0;
    *(unsigned __int64 *)(v_stack_mC0 + 80) = v_xmm1;
    *(unsigned __int64 *)(v_stack_mC0 + 96) = v_xmm0;
    *(unsigned __int64 *)(v_stack_mC0 + 112) = v_xmm0;
    *(unsigned __int64 *)(v_stack_mC0 + 128) = v_xmm1;
    *(unsigned __int64 *)(v_stack_mC0 + 144) = v_xmm0;
    v_stack_mE0 = (unsigned int)((unsigned int)(a6));
    v_stack_mE8 = *(unsigned __int64 *)(a5);
    if (a1 == 0) goto loc_00A35033;
    result = sub_0040C2C0(v_stack_mC8, a2, a3, a4);
loc_00A35018:
    result = 0;
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (264);
    return result;
loc_00A35033:
    result = sub_0040C640(a1, a2, a3, a4);
    goto loc_00A35018;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00A34F4C(int32_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, void *Arg5, uint32_t Arg6, void *Arg7, uint64_t Arg8, int64_t Arg9)
{
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mE0;
    uint64_t v_stack_mE8;

    local_rsp = (local_rsp) - (264);
    result = (*(uint64_t *)(v_rip + 0x3D57E6)) ^ (local_rsp);
    v_stack_m18 = result;
    v_stack_mC8 = v_rip - 10691972;
    v_stack_mD8 = Arg9;
    *(uint64_t *)(v_stack_mC0) = v_xmm0;
    *(uint64_t *)(v_stack_mC0 + 0x10) = v_xmm1;
    *(uint64_t *)(v_stack_mC0 + 0x20) = v_xmm0;
    *(uint64_t *)(v_stack_mC0 + 0x30) = v_xmm1;
    *(uint64_t *)(v_stack_mC0 + 0x40) = v_xmm0;
    *(uint64_t *)(v_stack_mC0 + 0x50) = v_xmm1;
    *(uint64_t *)(v_stack_mC0 + 0x60) = v_xmm0;
    *(uint64_t *)(v_stack_mC0 + 0x70) = v_xmm0;
    *(uint64_t *)(v_stack_mC0 + 0x80) = v_xmm1;
    *(uint64_t *)(v_stack_mC0 + 0x90) = v_xmm0;
    v_stack_mE0 = (uint32_t)((uint32_t)(Arg6));
    v_stack_mE8 = *(uint64_t *)(arg5);
    if (Arg1 == 0) goto loc_00A35033;
    result = sub_0040C2C0(v_stack_mC8, Arg2, Arg3, Arg4);
loc_00A35018:
    result = 0;
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (264);
    return result;
loc_00A35033:
    result = sub_0040C640(Arg1, Arg2, Arg3, Arg4);
    goto loc_00A35018;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg5` | `+ 0x0` | `64` | `R` |
| `Arg7` | `+ 0x0` | `128` | `R` |
| `Arg7` | `+ 0x10` | `128` | `R` |
| `Arg7` | `+ 0x20` | `128` | `R` |
| `Arg7` | `+ 0x30` | `128` | `R` |
| `Arg7` | `+ 0x40` | `128` | `R` |
| `Arg7` | `+ 0x50` | `128` | `R` |
| `Arg7` | `+ 0x60` | `128` | `R` |
| `Arg7` | `+ 0x70` | `128` | `R` |
| `Arg7` | `+ 0x80` | `128` | `R` |
| `Arg7` | `+ 0x90` | `128` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A34F4C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A34F4C[BB_00A34F4C]
  bb_00A35013[BB_00A35013]
  bb_00A35018[BB_00A35018]
  bb_00A35032[BB_00A35032]
  bb_00A35033[BB_00A35033]
  bb_00A34F4C -->|branch| bb_00A35033
  bb_00A34F4C -->|fallthrough| bb_00A35013
  bb_00A35013 -->|flow| bb_00A35018
  bb_00A35032 -->|flow| bb_00A35033
  bb_00A35033 -->|branch| bb_00A35018
```
