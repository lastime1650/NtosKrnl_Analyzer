# SymCryptFdefModMulMontgomeryMulx256Asm

- RVA: `0x00530290`–`0x005305CE` (길이 `830` bytes)
- VA: `0x0000000140530290`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C3530`
- 디코드: `173`개 명령, `830/830` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [SymCryptFdefModSetPostMontgomeryMulx256](SymCryptFdefModSetPostMontgomeryMulx256_function_00535140.md) at `0x0053514E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00530290  48 56                           push rsi
00530292  57                              push rdi
00530293  55                              push rbp
00530294  53                              push rbx
00530295  41 54                           push r12
00530297  41 55                           push r13
00530299  41 56                           push r14
0053029B  4C 8B D2                        mov r10, rdx
0053029E  4D 33 ED                        xor r13, r13
005302A1  49 8B 12                        mov rdx, qword ptr [r10]
005302A4  C4 C2 CB F6 38                  mulx rdi, rsi, qword ptr [r8]
005302A9  C4 C2 FB F6 68 08               mulx rbp, rax, qword ptr [r8 + 8]
005302AF  48 13 F8                        adc rdi, rax
005302B2  C4 C2 FB F6 58 10               mulx rbx, rax, qword ptr [r8 + 0x10]
005302B8  48 13 E8                        adc rbp, rax
005302BB  C4 42 FB F6 60 18               mulx r12, rax, qword ptr [r8 + 0x18]
005302C1  48 13 D8                        adc rbx, rax
005302C4  4D 13 E5                        adc r12, r13
005302C7  4C 8B F6                        mov r14, rsi
005302CA  4C 0F AF 71 18                  imul r14, qword ptr [rcx + 0x18]
005302CF  48 81 C1 80 00 00 00            add rcx, 0x80
005302D6  49 8B 52 08                     mov rdx, qword ptr [r10 + 8]
005302DA  48 33 C0                        xor rax, rax
005302DD  C4 42 FB F6 18                  mulx r11, rax, qword ptr [r8]
005302E2  F3 48 0F 38 F6 F8               adox rdi, rax
005302E8  66 49 0F 38 F6 EB               adcx rbp, r11
005302EE  C4 42 FB F6 58 08               mulx r11, rax, qword ptr [r8 + 8]
005302F4  F3 48 0F 38 F6 E8               adox rbp, rax
005302FA  66 49 0F 38 F6 DB               adcx rbx, r11
00530300  C4 42 FB F6 58 10               mulx r11, rax, qword ptr [r8 + 0x10]
00530306  F3 48 0F 38 F6 D8               adox rbx, rax
0053030C  66 4D 0F 38 F6 E3               adcx r12, r11
00530312  C4 42 FB F6 58 18               mulx r11, rax, qword ptr [r8 + 0x18]
00530318  F3 4C 0F 38 F6 E0               adox r12, rax
0053031E  48 C7 C0 00 00 00 00            mov rax, 0
00530325  66 4C 0F 38 F6 D8               adcx r11, rax
0053032B  F3 4C 0F 38 F6 E8               adox r13, rax
00530331  48 33 C0                        xor rax, rax
00530334  49 8B D6                        mov rdx, r14
00530337  C4 62 FB F6 31                  mulx r14, rax, qword ptr [rcx]
0053033C  66 48 0F 38 F6 F0               adcx rsi, rax
00530342  F3 49 0F 38 F6 FE               adox rdi, r14
00530348  C4 62 FB F6 71 08               mulx r14, rax, qword ptr [rcx + 8]
0053034E  66 48 0F 38 F6 F8               adcx rdi, rax
00530354  F3 49 0F 38 F6 EE               adox rbp, r14
0053035A  C4 62 FB F6 71 10               mulx r14, rax, qword ptr [rcx + 0x10]
00530360  66 48 0F 38 F6 E8               adcx rbp, rax
00530366  F3 49 0F 38 F6 DE               adox rbx, r14
0053036C  C4 62 FB F6 71 18               mulx r14, rax, qword ptr [rcx + 0x18]
00530372  66 48 0F 38 F6 D8               adcx rbx, rax
00530378  F3 4D 0F 38 F6 E6               adox r12, r14
0053037E  66 4C 0F 38 F6 E6               adcx r12, rsi
00530384  F3 4C 0F 38 F6 EE               adox r13, rsi
0053038A  4D 13 EB                        adc r13, r11
0053038D  48 13 F6                        adc rsi, rsi
00530390  4C 8B F7                        mov r14, rdi
00530393  4C 0F AF 71 98                  imul r14, qword ptr [rcx - 0x68]
00530398  49 8B 52 10                     mov rdx, qword ptr [r10 + 0x10]
0053039C  48 33 C0                        xor rax, rax
0053039F  C4 42 FB F6 18                  mulx r11, rax, qword ptr [r8]
005303A4  F3 48 0F 38 F6 E8               adox rbp, rax
005303AA  66 49 0F 38 F6 DB               adcx rbx, r11
005303B0  C4 42 FB F6 58 08               mulx r11, rax, qword ptr [r8 + 8]
005303B6  F3 48 0F 38 F6 D8               adox rbx, rax
005303BC  66 4D 0F 38 F6 E3               adcx r12, r11
005303C2  C4 42 FB F6 58 10               mulx r11, rax, qword ptr [r8 + 0x10]
005303C8  F3 4C 0F 38 F6 E0               adox r12, rax
005303CE  66 4D 0F 38 F6 EB               adcx r13, r11
005303D4  C4 42 FB F6 58 18               mulx r11, rax, qword ptr [r8 + 0x18]
005303DA  F3 4C 0F 38 F6 E8               adox r13, rax
005303E0  48 C7 C0 00 00 00 00            mov rax, 0
005303E7  66 4C 0F 38 F6 D8               adcx r11, rax
005303ED  F3 48 0F 38 F6 F0               adox rsi, rax
005303F3  48 33 C0                        xor rax, rax
005303F6  49 8B D6                        mov rdx, r14
005303F9  C4 62 FB F6 31                  mulx r14, rax, qword ptr [rcx]
005303FE  66 48 0F 38 F6 F8               adcx rdi, rax
00530404  F3 49 0F 38 F6 EE               adox rbp, r14
0053040A  C4 62 FB F6 71 08               mulx r14, rax, qword ptr [rcx + 8]
00530410  66 48 0F 38 F6 E8               adcx rbp, rax
00530416  F3 49 0F 38 F6 DE               adox rbx, r14
0053041C  C4 62 FB F6 71 10               mulx r14, rax, qword ptr [rcx + 0x10]
00530422  66 48 0F 38 F6 D8               adcx rbx, rax
00530428  F3 4D 0F 38 F6 E6               adox r12, r14
0053042E  C4 62 FB F6 71 18               mulx r14, rax, qword ptr [rcx + 0x18]
00530434  66 4C 0F 38 F6 E0               adcx r12, rax
0053043A  F3 4D 0F 38 F6 EE               adox r13, r14
00530440  66 4C 0F 38 F6 EF               adcx r13, rdi
00530446  F3 48 0F 38 F6 F7               adox rsi, rdi
0053044C  49 13 F3                        adc rsi, r11
0053044F  48 13 FF                        adc rdi, rdi
00530452  4C 8B F5                        mov r14, rbp
00530455  4C 0F AF 71 98                  imul r14, qword ptr [rcx - 0x68]
0053045A  49 8B 52 18                     mov rdx, qword ptr [r10 + 0x18]
0053045E  48 33 C0                        xor rax, rax
00530461  C4 42 FB F6 18                  mulx r11, rax, qword ptr [r8]
00530466  F3 48 0F 38 F6 D8               adox rbx, rax
0053046C  66 4D 0F 38 F6 E3               adcx r12, r11
00530472  C4 42 FB F6 58 08               mulx r11, rax, qword ptr [r8 + 8]
00530478  F3 4C 0F 38 F6 E0               adox r12, rax
0053047E  66 4D 0F 38 F6 EB               adcx r13, r11
00530484  C4 42 FB F6 58 10               mulx r11, rax, qword ptr [r8 + 0x10]
0053048A  F3 4C 0F 38 F6 E8               adox r13, rax
00530490  66 49 0F 38 F6 F3               adcx rsi, r11
00530496  C4 42 FB F6 58 18               mulx r11, rax, qword ptr [r8 + 0x18]
0053049C  F3 48 0F 38 F6 F0               adox rsi, rax
005304A2  48 C7 C0 00 00 00 00            mov rax, 0
005304A9  66 4C 0F 38 F6 D8               adcx r11, rax
005304AF  F3 48 0F 38 F6 F8               adox rdi, rax
005304B5  48 33 C0                        xor rax, rax
005304B8  49 8B D6                        mov rdx, r14
005304BB  C4 62 FB F6 31                  mulx r14, rax, qword ptr [rcx]
005304C0  66 48 0F 38 F6 E8               adcx rbp, rax
005304C6  F3 49 0F 38 F6 DE               adox rbx, r14
005304CC  C4 62 FB F6 71 08               mulx r14, rax, qword ptr [rcx + 8]
005304D2  66 48 0F 38 F6 D8               adcx rbx, rax
005304D8  F3 4D 0F 38 F6 E6               adox r12, r14
005304DE  C4 62 FB F6 71 10               mulx r14, rax, qword ptr [rcx + 0x10]
005304E4  66 4C 0F 38 F6 E0               adcx r12, rax
005304EA  F3 4D 0F 38 F6 EE               adox r13, r14
005304F0  C4 62 FB F6 71 18               mulx r14, rax, qword ptr [rcx + 0x18]
005304F6  66 4C 0F 38 F6 E8               adcx r13, rax
005304FC  F3 49 0F 38 F6 F6               adox rsi, r14
00530502  66 48 0F 38 F6 F5               adcx rsi, rbp
00530508  F3 48 0F 38 F6 FD               adox rdi, rbp
0053050E  49 13 FB                        adc rdi, r11
00530511  48 13 ED                        adc rbp, rbp
00530514  4C 8B F3                        mov r14, rbx
00530517  4C 0F AF 71 98                  imul r14, qword ptr [rcx - 0x68]
0053051C  48 33 C0                        xor rax, rax
0053051F  49 8B D6                        mov rdx, r14
00530522  C4 62 FB F6 19                  mulx r11, rax, qword ptr [rcx]
00530527  66 48 0F 38 F6 D8               adcx rbx, rax
0053052D  F3 4D 0F 38 F6 E3               adox r12, r11
00530533  C4 62 FB F6 59 08               mulx r11, rax, qword ptr [rcx + 8]
00530539  66 4C 0F 38 F6 E0               adcx r12, rax
0053053F  F3 4D 0F 38 F6 EB               adox r13, r11
00530545  C4 62 FB F6 59 10               mulx r11, rax, qword ptr [rcx + 0x10]
0053054B  66 4C 0F 38 F6 E8               adcx r13, rax
00530551  F3 49 0F 38 F6 F3               adox rsi, r11
00530557  C4 62 FB F6 59 18               mulx r11, rax, qword ptr [rcx + 0x18]
0053055D  66 48 0F 38 F6 F0               adcx rsi, rax
00530563  F3 49 0F 38 F6 FB               adox rdi, r11
00530569  48 C7 C0 00 00 00 00            mov rax, 0
00530570  66 48 0F 38 F6 F8               adcx rdi, rax
00530576  F3 48 0F 38 F6 E8               adox rbp, rax
0053057C  48 13 E8                        adc rbp, rax
0053057F  48 81 C1 80 00 00 00            add rcx, 0x80
00530586  48 8B 01                        mov rax, qword ptr [rcx]
00530589  49 03 C4                        add rax, r12
0053058C  4C 8B 51 08                     mov r10, qword ptr [rcx + 8]
00530590  4D 13 D5                        adc r10, r13
00530593  4C 8B 41 10                     mov r8, qword ptr [rcx + 0x10]
00530597  4C 13 C6                        adc r8, rsi
0053059A  4C 8B 59 18                     mov r11, qword ptr [rcx + 0x18]
0053059E  4C 13 DF                        adc r11, rdi
005305A1  48 13 ED                        adc rbp, rbp
005305A4  4C 0F 45 E0                     cmovne r12, rax
005305A8  4D 0F 45 EA                     cmovne r13, r10
005305AC  49 0F 45 F0                     cmovne rsi, r8
005305B0  49 0F 45 FB                     cmovne rdi, r11
005305B4  4D 89 21                        mov qword ptr [r9], r12
005305B7  4D 89 69 08                     mov qword ptr [r9 + 8], r13
005305BB  49 89 71 10                     mov qword ptr [r9 + 0x10], rsi
005305BF  49 89 79 18                     mov qword ptr [r9 + 0x18], rdi
005305C3  41 5E                           pop r14
005305C5  41 5D                           pop r13
005305C7  41 5C                           pop r12
005305C9  5B                              pop rbx
005305CA  5D                              pop rbp
005305CB  5F                              pop rdi
005305CC  5E                              pop rsi
005305CD  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptFdefModMulMontgomeryMulx256Asm(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;

    v_r13 = 0;
    v_r14 = (v_rsi) * (*(unsigned __int64 *)(a1 + 24));
    a1 = (a1) + (128);
    result = 0;
    result = 0;
    v_r14 = (v_rdi) * (*(unsigned __int64 *)(a1 - 104));
    result = 0;
    result = 0;
    v_r14 = (v_rbp) * (*(unsigned __int64 *)(a1 - 104));
    result = 0;
    result = 0;
    v_r14 = (v_rbx) * (*(unsigned __int64 *)(a1 - 104));
    result = 0;
    a1 = (a1) + (128);
    result = (*(unsigned __int64 *)(a1)) + (v_r12);
    if (condition_is_not_equal) {
        v_r12 = result;
        v_r13 = *(unsigned __int64 *)(a1 + 8);
        v_rsi = *(unsigned __int64 *)(a1 + 16);
        v_rdi = *(unsigned __int64 *)(a1 + 24);
    }
    *(unsigned __int64 *)(a4) = v_r12;
    *(unsigned __int64 *)(a4 + 8) = v_r13;
    *(unsigned __int64 *)(a4 + 16) = v_rsi;
    *(unsigned __int64 *)(a4 + 24) = v_rdi;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptFdefModMulMontgomeryMulx256Asm(void *Arg1, void *Arg2, void *Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;

    local_r13 = 0;
    local_r14 = (local_rsi) * (*(uint64_t *)(arg1 + 0x18));
    Arg1 = (Arg1) + (128);
    result = 0;
    result = 0;
    local_r14 = (local_rdi) * (*(uint64_t *)(arg1 - 0x68));
    result = 0;
    result = 0;
    local_r14 = (local_rbp) * (*(uint64_t *)(arg1 - 0x68));
    result = 0;
    result = 0;
    local_r14 = (local_rbx) * (*(uint64_t *)(arg1 - 0x68));
    result = 0;
    Arg1 = (Arg1) + (128);
    result = (*(uint64_t *)(arg1)) + (local_r12);
    if (condition_is_not_equal) {
        local_r12 = result;
        local_r13 = *(uint64_t *)(arg1 + 0x8);
        local_rsi = *(uint64_t *)(arg1 + 0x10);
        local_rdi = *(uint64_t *)(arg1 + 0x18);
    }
    *(uint64_t *)(arg4) = local_r12;
    *(uint64_t *)(arg4 + 0x8) = local_r13;
    *(uint64_t *)(arg4 + 0x10) = local_rsi;
    *(uint64_t *)(arg4 + 0x18) = local_rdi;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x68` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x8` | `64` | `R` |
| `Arg3` | `+ 0x10` | `64` | `R` |
| `Arg3` | `+ 0x18` | `64` | `R` |
| `Arg4` | `+ 0x0` | `64` | `W` |
| `Arg4` | `+ 0x8` | `64` | `W` |
| `Arg4` | `+ 0x10` | `64` | `W` |
| `Arg4` | `+ 0x18` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00530290&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00530290[BB_00530290]
```
