# EmonEnableMonitoringOriginal

- RVA: `0x0055CA40`–`0x0055CB97` (길이 `343` bytes)
- VA: `0x000000014055CA40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00086C3C`
- 디코드: `94`개 명령, `343/343` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0055CA7A` → [HalpAcquireHighLevelLock](../2D/HalpAcquireHighLevelLock_function_002D2390.md) (function, `0x002D2390`)
- `0x0055CA8A` → [HalpGetProfileDescriptor](../4B/HalpGetProfileDescriptor_function_004BB170.md) (function, `0x004BB170`)
- `0x0055CAB4` → [HalpGetProfileDescriptor](../4B/HalpGetProfileDescriptor_function_004BB170.md) (function, `0x004BB170`)
- `0x0055CAD4` → [KeCheckProcessorAffinityEx](../30/KeCheckProcessorAffinityEx_function_00305150.md) (function, `0x00305150`)
- `0x0055CB02` → [EmonAllocateCounterOriginal](EmonAllocateCounterOriginal_function_0055C24C.md) (function, `0x0055C24C`)
- `0x0055CB68` → [EmonConfigureCounter](EmonConfigureCounter_function_0055C590.md) (function, `0x0055C590`)
- `0x0055CB77` → [HalpReleaseHighLevelLock](../2D/HalpReleaseHighLevelLock_function_002D1C58.md) (function, `0x002D1C58`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0055CA64` → RVA `0x00FC2BD0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0055CA40  48 8B C4                        mov rax, rsp
0055CA43  48 89 58 08                     mov qword ptr [rax + 8], rbx
0055CA47  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
0055CA4B  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
0055CA4F  55                              push rbp
0055CA50  56                              push rsi
0055CA51  57                              push rdi
0055CA52  41 54                           push r12
0055CA54  41 55                           push r13
0055CA56  41 56                           push r14
0055CA58  41 57                           push r15
0055CA5A  48 83 EC 50                     sub rsp, 0x50
0055CA5E  45 33 F6                        xor r14d, r14d
0055CA61  44 8B E1                        mov r12d, ecx
0055CA64  48 8D 0D 65 61 A6 00            lea rcx, [rip + 0xa66165]
0055CA6B  4C 89 70 B0                     mov qword ptr [rax - 0x50], r14
0055CA6F  4C 89 70 B8                     mov qword ptr [rax - 0x48], r14
0055CA73  44 8B FA                        mov r15d, edx
0055CA76  44 89 70 A8                     mov dword ptr [rax - 0x58], r14d
0055CA7A  E8 11 59 D7 FF                  call 0x1402d2390
0055CA7F  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
0055CA84  41 8B CF                        mov ecx, r15d
0055CA87  44 8A E8                        mov r13b, al
0055CA8A  E8 E1 E6 F5 FF                  call 0x1404bb170
0055CA8F  8B F8                           mov edi, eax
0055CA91  85 C0                           test eax, eax
0055CA93  0F 88 D4 00 00 00               js 0x14055cb6d
0055CA99  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
0055CA9E  48 8B F3                        mov rsi, rbx
0055CAA1  48 8B EB                        mov rbp, rbx
0055CAA4  8B 8B 38 01 00 00               mov ecx, dword ptr [rbx + 0x138]
0055CAAA  83 F9 25                        cmp ecx, 0x25
0055CAAD  74 19                           je 0x14055cac8
0055CAAF  4C 8D 44 24 40                  lea r8, [rsp + 0x40]
0055CAB4  E8 B7 E6 F5 FF                  call 0x1404bb170
0055CAB9  85 C0                           test eax, eax
0055CABB  78 0B                           js 0x14055cac8
0055CABD  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
0055CAC2  48 8B F3                        mov rsi, rbx
0055CAC5  48 8B EB                        mov rbp, rbx
0055CAC8  65 8B 14 25 A4 01 00 00         mov edx, dword ptr gs:[0x1a4]
0055CAD0  48 8D 4B 20                     lea rcx, [rbx + 0x20]
0055CAD4  E8 77 86 DA FF                  call 0x140305150
0055CAD9  85 C0                           test eax, eax
0055CADB  75 0A                           jne 0x14055cae7
0055CADD  BF BB 00 00 C0                  mov edi, 0xc00000bb
0055CAE2  E9 86 00 00 00                  jmp 0x14055cb6d
0055CAE7  4C 8B B4 24 B8 00 00 00         mov r14, qword ptr [rsp + 0xb8]
0055CAEF  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
0055CAF4  45 8B C7                        mov r8d, r15d
0055CAF7  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
0055CAFC  48 8B D3                        mov rdx, rbx
0055CAFF  41 8B CC                        mov ecx, r12d
0055CB02  E8 45 F7 FF FF                  call 0x14055c24c
0055CB07  8B F8                           mov edi, eax
0055CB09  85 C0                           test eax, eax
0055CB0B  78 60                           js 0x14055cb6d
0055CB0D  44 8B 54 24 30                  mov r10d, dword ptr [rsp + 0x30]
0055CB12  45 85 E4                        test r12d, r12d
0055CB15  45 8B C2                        mov r8d, r10d
0055CB18  0F 94 C2                        sete dl
0055CB1B  41 83 3E 01                     cmp dword ptr [r14], 1
0055CB1F  75 08                           jne 0x14055cb29
0055CB21  41 0F BA E8 1E                  bts r8d, 0x1e
0055CB26  48 8B F5                        mov rsi, rbp
0055CB29  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
0055CB31  41 8B CA                        mov ecx, r10d
0055CB34  88 54 24 28                     mov byte ptr [rsp + 0x28], dl
0055CB38  44 89 00                        mov dword ptr [rax], r8d
0055CB3B  41 B0 01                        mov r8b, 1
0055CB3E  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
0055CB46  44 89 10                        mov dword ptr [rax], r10d
0055CB49  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
0055CB51  C7 00 01 00 00 00               mov dword ptr [rax], 1
0055CB57  8B 83 30 01 00 00               mov eax, dword ptr [rbx + 0x130]
0055CB5D  44 8B 4E 18                     mov r9d, dword ptr [rsi + 0x18]
0055CB61  41 8B 16                        mov edx, dword ptr [r14]
0055CB64  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0055CB68  E8 23 FA FF FF                  call 0x14055c590
0055CB6D  41 8A D5                        mov dl, r13b
0055CB70  48 8D 0D 59 60 A6 00            lea rcx, [rip + 0xa66059]
0055CB77  E8 DC 50 D7 FF                  call 0x1402d1c58
0055CB7C  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
0055CB84  8B C7                           mov eax, edi
0055CB86  48 83 C4 50                     add rsp, 0x50
0055CB8A  41 5F                           pop r15
0055CB8C  41 5E                           pop r14
0055CB8E  41 5D                           pop r13
0055CB90  41 5C                           pop r12
0055CB92  5F                              pop rdi
0055CB93  5E                              pop rsi
0055CB94  5D                              pop rbp
0055CB95  C3                              ret
0055CB96  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EmonEnableMonitoringOriginal(int a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int8 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (80);
    v_r14 = 0;
    *(unsigned __int64 *)(v_rsp - 80) = 0;
    *(unsigned __int64 *)(v_rsp - 72) = 0;
    *(unsigned int *)(v_rsp - 88) = 0;
    result = HalpAcquireHighLevelLock(v_rip + 10903909, a2, a3, a4);
    result = HalpGetProfileDescriptor((unsigned int)((unsigned int)((unsigned int)(a2))), a2, v_stack_m50, a4);
    if (sign_flag) goto loc_0055CB6D;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m50 + 312)))) == 37) goto loc_0055CAC8;
    result = HalpGetProfileDescriptor((unsigned int)(*(unsigned int *)(v_stack_m50 + 312)), a2, v_stack_m48, a4);
    v_rbx = v_stack_m50;
    v_rsi = v_stack_m50;
    v_rbp = v_stack_m50;
    if (!(sign_flag)) {
        v_rbx = v_stack_m48;
        v_rsi = v_rbx;
        v_rbp = v_rbx;
    }
    result = KeCheckProcessorAffinityEx(v_rbx + 32, (unsigned int)(*(unsigned int *)(gs_base + (0 + 420))), v_stack_m48, a4);
    if ((unsigned int)(result) != 0) goto loc_0055CAE7;
    goto loc_0055CB6D;
loc_0055CAE7:
    v_stack_m68 = a6;
    result = EmonAllocateCounterOriginal((unsigned int)((unsigned int)((unsigned int)(a1))), v_rbx, (unsigned int)((unsigned int)((unsigned int)(a2))), v_stack_m58);
    if (sign_flag) goto loc_0055CB6D;
    a2 = ((unsigned int)((unsigned int)(a1)) == 0) ? 1 : 0;
    if ((*(unsigned int *)(a6)) == 1) {
        v_rsi = v_rbp;
    }
    v_stack_m60 = (unsigned __int8)(a2);
    *(unsigned int *)(a5) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m58))));
    *(unsigned int *)(v_stack_p20) = (unsigned int)((unsigned int)(v_stack_m58));
    *(unsigned int *)(v_stack_p18) = 1;
    v_stack_m68 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 304)));
    result = EmonConfigureCounter((unsigned int)((unsigned int)((unsigned int)(v_stack_m58))), (unsigned int)(*(unsigned int *)(a6)), 1, (unsigned int)(*(unsigned int *)(v_rsi + 24)));
loc_0055CB6D:
    result = HalpReleaseHighLevelLock(v_rip + 10903641, (unsigned __int8)((unsigned __int8)(result)), 1, (unsigned int)(*(unsigned int *)(v_rsi + 24)));
    v_rsp = (v_rsp) + (80);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t EmonEnableMonitoringOriginal(int32_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, void *Arg5, void *Arg6)
{
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint8_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (80);
    local_r14 = 0;
    *(uint64_t *)(local_rsp - 0x50) = 0;
    *(uint64_t *)(local_rsp - 0x48) = 0;
    *(uint32_t *)(local_rsp - 0x58) = 0;
    result = HalpAcquireHighLevelLock(v_rip + 10903909, Arg2, Arg3, Arg4);
    result = HalpGetProfileDescriptor((uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg2, v_stack_m50, Arg4);
    if (sign_flag) goto loc_0055CB6D;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m50 + 0x138)))) == 37) goto loc_0055CAC8;
    result = HalpGetProfileDescriptor((uint32_t)(*(uint32_t *)(v_stack_m50 + 0x138)), Arg2, v_stack_m48, Arg4);
    local_rbx = v_stack_m50;
    local_rsi = v_stack_m50;
    local_rbp = v_stack_m50;
    if (!(sign_flag)) {
        local_rbx = v_stack_m48;
        local_rsi = local_rbx;
        local_rbp = local_rbx;
    }
    result = KeCheckProcessorAffinityEx(local_rbx + 32, (uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))), v_stack_m48, Arg4);
    if ((uint32_t)(result) != 0) goto loc_0055CAE7;
    goto loc_0055CB6D;
loc_0055CAE7:
    v_stack_m68 = Arg6;
    result = EmonAllocateCounterOriginal((uint32_t)((uint32_t)((uint32_t)(Arg1))), local_rbx, (uint32_t)((uint32_t)((uint32_t)(Arg2))), v_stack_m58);
    if (sign_flag) goto loc_0055CB6D;
    Arg2 = ((uint32_t)((uint32_t)(Arg1)) == 0) ? 1 : 0;
    if ((*(uint32_t *)(arg6)) == 1) {
        local_rsi = local_rbp;
    }
    v_stack_m60 = (uint8_t)(Arg2);
    *(uint32_t *)(arg5) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m58))));
    *(uint32_t *)(v_stack_p20) = (uint32_t)((uint32_t)(v_stack_m58));
    *(uint32_t *)(v_stack_p18) = 1;
    v_stack_m68 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x130)));
    result = EmonConfigureCounter((uint32_t)((uint32_t)((uint32_t)(v_stack_m58))), (uint32_t)(*(uint32_t *)(arg6)), 1, (uint32_t)(*(uint32_t *)(local_rsi + 0x18)));
loc_0055CB6D:
    result = HalpReleaseHighLevelLock(v_rip + 10903641, (uint8_t)((uint8_t)(result)), 1, (uint32_t)(*(uint32_t *)(local_rsi + 0x18)));
    local_rsp = (local_rsp) + (80);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg5` | `+ 0x0` | `32` | `W` |
| `Arg6` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0055CA40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0055CA40[BB_0055CA40]
  bb_0055CA99[BB_0055CA99]
  bb_0055CAAF[BB_0055CAAF]
  bb_0055CABD[BB_0055CABD]
  bb_0055CAC8[BB_0055CAC8]
  bb_0055CADD[BB_0055CADD]
  bb_0055CAE7[BB_0055CAE7]
  bb_0055CB0D[BB_0055CB0D]
  bb_0055CB21[BB_0055CB21]
  bb_0055CB29[BB_0055CB29]
  bb_0055CB6D[BB_0055CB6D]
  bb_0055CB96[BB_0055CB96]
  bb_0055CA40 -->|branch| bb_0055CB6D
  bb_0055CA40 -->|fallthrough| bb_0055CA99
  bb_0055CA99 -->|branch| bb_0055CAC8
  bb_0055CA99 -->|fallthrough| bb_0055CAAF
  bb_0055CAAF -->|branch| bb_0055CAC8
  bb_0055CAAF -->|fallthrough| bb_0055CABD
  bb_0055CABD -->|flow| bb_0055CAC8
  bb_0055CAC8 -->|branch| bb_0055CAE7
  bb_0055CAC8 -->|fallthrough| bb_0055CADD
  bb_0055CADD -->|branch| bb_0055CB6D
  bb_0055CAE7 -->|branch| bb_0055CB6D
  bb_0055CAE7 -->|fallthrough| bb_0055CB0D
  bb_0055CB0D -->|branch| bb_0055CB29
  bb_0055CB0D -->|fallthrough| bb_0055CB21
  bb_0055CB21 -->|flow| bb_0055CB29
  bb_0055CB29 -->|flow| bb_0055CB6D
```
