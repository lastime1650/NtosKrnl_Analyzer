# PfSnLogVolumeCreate

- RVA: `0x00960AE0`–`0x00960C15` (길이 `309` bytes)
- VA: `0x0000000140960AE0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000931DC`
- 디코드: `88`개 명령, `309/309` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00960B1F` → [PfSnLogHelper](PfSnLogHelper_function_00960C1C.md) (function, `0x00960C1C`)
- `0x00960B63` → [PfSnGetNLLogEntry](PfSnGetNLLogEntry_function_00960D38.md) (function, `0x00960D38`)
- `0x00960BD6` → [RtlUpcaseUnicodeString](RtlUpcaseUnicodeString_function_00960780.md) (function, `0x00960780`)
- `0x00960BEC` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- [sub_00342A1A](../../text/34/Unknown_function_00342A1A.md) at `0x00342A1E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00960BEC` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00960AE0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00960AE5  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00960AEA  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00960AEF  55                              push rbp
00960AF0  41 56                           push r14
00960AF2  41 57                           push r15
00960AF4  48 8B EC                        mov rbp, rsp
00960AF7  48 83 EC 50                     sub rsp, 0x50
00960AFB  0F B7 71 1E                     movzx esi, word ptr [rcx + 0x1e]
00960AFF  4C 8D 45 20                     lea r8, [rbp + 0x20]
00960B03  33 FF                           xor edi, edi
00960B05  4C 8B F1                        mov r14, rcx
00960B08  48 8B 09                        mov rcx, qword ptr [rcx]
00960B0B  03 F6                           add esi, esi
00960B0D  89 7D F4                        mov dword ptr [rbp - 0xc], edi
00960B10  89 7D E4                        mov dword ptr [rbp - 0x1c], edi
00960B13  48 89 7D 20                     mov qword ptr [rbp + 0x20], rdi
00960B17  8D 5E 61                        lea ebx, [rsi + 0x61]
00960B1A  C1 EB 04                        shr ebx, 4
00960B1D  8B D3                           mov edx, ebx
00960B1F  E8 F8 00 00 00                  call 0x140960c1c
00960B24  4C 8B F8                        mov r15, rax
00960B27  48 85 C0                        test rax, rax
00960B2A  0F 84 DE 00 00 00               je 0x140960c0e
00960B30  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00960B34  8D 53 FF                        lea edx, [rbx - 1]
00960B37  48 8B 4D 20                     mov rcx, qword ptr [rbp + 0x20]
00960B3B  0F 57 C0                        xorps xmm0, xmm0
00960B3E  48 C1 E2 04                     shl rdx, 4
00960B42  48 83 CA 05                     or rdx, 5
00960B46  0F 11 01                        movups xmmword ptr [rcx], xmm0
00960B49  48 89 11                        mov qword ptr [rcx], rdx
00960B4C  8D 57 02                        lea edx, [rdi + 2]
00960B4F  4C 89 41 08                     mov qword ptr [rcx + 8], r8
00960B53  44 8D 46 42                     lea r8d, [rsi + 0x42]
00960B57  41 8B 46 38                     mov eax, dword ptr [r14 + 0x38]
00960B5B  45 8B 4E 34                     mov r9d, dword ptr [r14 + 0x34]
00960B5F  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00960B63  E8 D0 01 00 00                  call 0x140960d38
00960B68  48 8B D8                        mov rbx, rax
00960B6B  66 89 7D F0                     mov word ptr [rbp - 0x10], di
00960B6F  48 83 C0 38                     add rax, 0x38
00960B73  66 89 75 F2                     mov word ptr [rbp - 0xe], si
00960B77  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00960B7B  48 8D 55 E0                     lea rdx, [rbp - 0x20]
00960B7F  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
00960B83  45 33 C0                        xor r8d, r8d
00960B86  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00960B8A  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00960B8E  48 89 43 18                     mov qword ptr [rbx + 0x18], rax
00960B92  8B 43 24                        mov eax, dword ptr [rbx + 0x24]
00960B95  8B C8                           mov ecx, eax
00960B97  41 33 4E 30                     xor ecx, dword ptr [r14 + 0x30]
00960B9B  83 E1 0F                        and ecx, 0xf
00960B9E  66 89 75 E0                     mov word ptr [rbp - 0x20], si
00960BA2  33 C8                           xor ecx, eax
00960BA4  66 89 75 E2                     mov word ptr [rbp - 0x1e], si
00960BA8  89 4B 24                        mov dword ptr [rbx + 0x24], ecx
00960BAB  8B C1                           mov eax, ecx
00960BAD  41 33 46 30                     xor eax, dword ptr [r14 + 0x30]
00960BB1  25 F0 00 00 00                  and eax, 0xf0
00960BB6  33 C1                           xor eax, ecx
00960BB8  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00960BBC  89 43 24                        mov dword ptr [rbx + 0x24], eax
00960BBF  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00960BC3  48 89 43 10                     mov qword ptr [rbx + 0x10], rax
00960BC7  41 8B 46 18                     mov eax, dword ptr [r14 + 0x18]
00960BCB  89 43 20                        mov dword ptr [rbx + 0x20], eax
00960BCE  66 89 73 28                     mov word ptr [rbx + 0x28], si
00960BD2  66 89 73 2A                     mov word ptr [rbx + 0x2a], si
00960BD6  E8 A5 FB FF FF                  call 0x140960780
00960BDB  41 0F B7 4E 1E                  movzx ecx, word ptr [r14 + 0x1e]
00960BE0  66 89 7C 4B 38                  mov word ptr [rbx + rcx*2 + 0x38], di
00960BE5  49 8D 8F 68 01 00 00            lea rcx, [r15 + 0x168]
00960BEC  E8 8F 92 9E FF                  call 0x140349e80
00960BF1  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
00960BF6  8B C7                           mov eax, edi
00960BF8  49 8B 5B 28                     mov rbx, qword ptr [r11 + 0x28]
00960BFC  49 8B 73 30                     mov rsi, qword ptr [r11 + 0x30]
00960C00  49 8B 7B 38                     mov rdi, qword ptr [r11 + 0x38]
00960C04  49 8B E3                        mov rsp, r11
00960C07  41 5F                           pop r15
00960C09  41 5E                           pop r14
00960C0B  5D                              pop rbp
00960C0C  C3                              ret
00960C0D  CC                              int3
00960C0E  BF 7A 01 00 C0                  mov edi, 0xc000017a
00960C13  EB DC                           jmp 0x140960bf1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfSnLogVolumeCreate(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m24;
    unsigned __int16 v_stack_m26;
    unsigned __int16 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned int v_stack_m34;
    unsigned __int16 v_stack_m36;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rsi;
    v_stack_p20 = v_rdi;
    v_rsp = (v_rsp) - (80);
    v_rdi = 0;
    v_rsi = (unsigned int)((*(unsigned __int16 *)(a1 + 30)) + ((unsigned int)(*(unsigned __int16 *)(a1 + 30))));
    v_stack_m24 = 0;
    v_stack_m34 = 0;
    v_stack_p8 = 0;
    v_rbx = (unsigned int)((v_rsi + 97) >> (4));
    result = PfSnLogHelper(*(unsigned __int64 *)(a1), (unsigned int)((unsigned int)(v_rbx)), v_stack_p8, a4);
    if (result == 0) goto loc_00960C0E;
    a2 = (v_rbx - 1) << (4);
    a2 = (a2) | (5);
    *(unsigned __int64 *)(v_stack_p8) = v_xmm0;
    *(unsigned __int64 *)(v_stack_p8) = a2;
    *(unsigned __int64 *)(v_stack_p8 + 8) = *(unsigned __int64 *)(a1 + 8);
    v_stack_m48 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 56)));
    result = PfSnGetNLLogEntry(v_stack_p8, v_rdi + 2, v_rsi + 66, (unsigned int)(*(unsigned int *)(a1 + 52)));
    v_stack_m28 = 0;
    result = (result) + (56);
    v_stack_m26 = (unsigned __int16)(v_rsi);
    v_stack_m20 = result;
    a3 = 0;
    v_stack_m30 = *(unsigned __int64 *)(a1 + 40);
    *(unsigned __int64 *)(result + 24) = *(unsigned __int64 *)(a1 + 8);
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 36))))) ^ (*(unsigned int *)(a1 + 48)));
    a1 = (unsigned int)((a1) & (15));
    v_stack_m38 = (unsigned __int16)(v_rsi);
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(result + 36)))));
    v_stack_m36 = (unsigned __int16)(v_rsi);
    *(unsigned int *)(result + 36) = (unsigned int)(a1);
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) ^ (*(unsigned int *)(a1 + 48)));
    result = (unsigned int)((result) & (240));
    result = (unsigned int)((result) ^ ((unsigned int)(a1)));
    *(unsigned int *)(result + 36) = (unsigned int)(result);
    *(unsigned __int64 *)(result + 16) = *(unsigned __int64 *)(a1 + 16);
    *(unsigned int *)(result + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)));
    *(unsigned __int16 *)(result + 40) = (unsigned __int16)(v_rsi);
    *(unsigned __int16 *)(result + 42) = (unsigned __int16)(v_rsi);
    result = RtlUpcaseUnicodeString(v_stack_m28, v_stack_m38, a3, (unsigned int)(*(unsigned int *)(a1 + 52)));
    *(unsigned __int16 *)(result + *(unsigned __int16 *)(a1 + 30) * 2 + 56) = 0;
    result = ExReleaseRundownProtection(result + 360, v_stack_m38, a3, (unsigned int)(*(unsigned int *)(a1 + 52)));
loc_00960BF1:
    return 0;
loc_00960C0E:
    goto loc_00960BF1;
}
```

## 5. (Beta) C Style

```c
int64_t PfSnLogVolumeCreate(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint32_t v_stack_m24;
    uint16_t v_stack_m26;
    uint16_t v_stack_m28;
    uint64_t v_stack_m30;
    uint32_t v_stack_m34;
    uint16_t v_stack_m36;
    uint64_t v_stack_m38;
    uint32_t v_stack_m48;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rsi;
    v_stack_p20 = local_rdi;
    local_rsp = (local_rsp) - (80);
    local_rdi = 0;
    local_rsi = (uint32_t)((*(uint16_t *)(arg1 + 0x1E)) + ((uint32_t)(*(uint16_t *)(arg1 + 0x1E))));
    v_stack_m24 = 0;
    v_stack_m34 = 0;
    v_stack_p8 = 0;
    local_rbx = (uint32_t)((local_rsi + 97) >> (4));
    result = PfSnLogHelper(*(uint64_t *)(arg1), (uint32_t)((uint32_t)(local_rbx)), v_stack_p8, a4);
    if (result == 0) goto loc_00960C0E;
    a2 = (local_rbx - 1) << (4);
    a2 = (a2) | (5);
    *(uint64_t *)(v_stack_p8) = v_xmm0;
    *(uint64_t *)(v_stack_p8) = a2;
    *(uint64_t *)(v_stack_p8 + 0x8) = *(uint64_t *)(arg1 + 0x8);
    v_stack_m48 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x38)));
    result = PfSnGetNLLogEntry(v_stack_p8, local_rdi + 2, local_rsi + 66, (uint32_t)(*(uint32_t *)(arg1 + 0x34)));
    v_stack_m28 = 0;
    result = (result) + (56);
    v_stack_m26 = (uint16_t)(local_rsi);
    v_stack_m20 = result;
    a3 = 0;
    v_stack_m30 = *(uint64_t *)(arg1 + 0x28);
    *(uint64_t *)(result + 0x18) = *(uint64_t *)(arg1 + 0x8);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x24))))) ^ (*(uint32_t *)(arg1 + 0x30)));
    Arg1 = (uint32_t)((Arg1) & (15));
    v_stack_m38 = (uint16_t)(local_rsi);
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x24)))));
    v_stack_m36 = (uint16_t)(local_rsi);
    *(uint32_t *)(result + 0x24) = (uint32_t)(Arg1);
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) ^ (*(uint32_t *)(arg1 + 0x30)));
    result = (uint32_t)((result) & (240));
    result = (uint32_t)((result) ^ ((uint32_t)(Arg1)));
    *(uint32_t *)(result + 0x24) = (uint32_t)(result);
    *(uint64_t *)(result + 0x10) = *(uint64_t *)(arg1 + 0x10);
    *(uint32_t *)(result + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)));
    *(uint16_t *)(result + 0x28) = (uint16_t)(local_rsi);
    *(uint16_t *)(result + 0x2A) = (uint16_t)(local_rsi);
    result = RtlUpcaseUnicodeString(v_stack_m28, v_stack_m38, a3, (uint32_t)(*(uint32_t *)(arg1 + 0x34)));
    *(uint16_t *)(result + *(uint16_t *)(arg1 + 0x1E) * 2 + 0x38) = 0;
    result = ExReleaseRundownProtection(result + 360, v_stack_m38, a3, (uint32_t)(*(uint32_t *)(arg1 + 0x34)));
loc_00960BF1:
    return 0;
loc_00960C0E:
    goto loc_00960BF1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x1E` | `16` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg1` | `+ 0x34` | `32` | `R` |
| `Arg1` | `+ 0x38` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00960AE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00960AE0[BB_00960AE0]
  bb_00960B30[BB_00960B30]
  bb_00960BF1[BB_00960BF1]
  bb_00960C0D[BB_00960C0D]
  bb_00960C0E[BB_00960C0E]
  bb_00960AE0 -->|branch| bb_00960C0E
  bb_00960AE0 -->|fallthrough| bb_00960B30
  bb_00960B30 -->|flow| bb_00960BF1
  bb_00960C0D -->|flow| bb_00960C0E
  bb_00960C0E -->|branch| bb_00960BF1
```
