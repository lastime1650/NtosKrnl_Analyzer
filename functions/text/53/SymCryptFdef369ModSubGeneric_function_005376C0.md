# SymCryptFdef369ModSubGeneric

- RVA: `0x005376C0`–`0x0053775E` (길이 `158` bytes)
- VA: `0x00000001405376C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007F3F8`
- 디코드: `43`개 명령, `158/158` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005376FE` → [EmpCheckErrataList](../49/EmpCheckErrataList_function_0049E550.md) (function, `0x0049E550`)
- `0x0053770F` → [SymCryptFdef369RawSubAsm](SymCryptFdef369RawSubAsm_function_0053B520.md) (function, `0x0053B520`)
- `0x00537728` → [SymCryptFdef369RawAddAsm](SymCryptFdef369RawAddAsm_function_0053B4D0.md) (function, `0x0053B4D0`)
- `0x0053773D` → [SymCryptFdef369MaskedCopyAsm](SymCryptFdef369MaskedCopyAsm_function_0053B570.md) (function, `0x0053B570`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005376C0  48 8B C4                        mov rax, rsp
005376C3  48 89 58 08                     mov qword ptr [rax + 8], rbx
005376C7  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
005376CB  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
005376CF  4C 89 70 20                     mov qword ptr [rax + 0x20], r14
005376D3  41 57                           push r15
005376D5  48 83 EC 20                     sub rsp, 0x20
005376D9  44 8B 71 04                     mov r14d, dword ptr [rcx + 4]
005376DD  49 8B D8                        mov rbx, r8
005376E0  45 8B C6                        mov r8d, r14d
005376E3  48 8B FA                        mov rdi, rdx
005376E6  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
005376EB  48 8B F1                        mov rsi, rcx
005376EE  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
005376F3  4D 8B F9                        mov r15, r9
005376F6  41 C1 E0 08                     shl r8d, 8
005376FA  41 83 C0 40                     add r8d, 0x40
005376FE  E8 4D 6E F6 FF                  call 0x14049e550
00537703  45 8B CE                        mov r9d, r14d
00537706  4D 8B C7                        mov r8, r15
00537709  48 8B D3                        mov rdx, rbx
0053770C  48 8B CF                        mov rcx, rdi
0053770F  E8 0C 3E 00 00                  call 0x14053b520
00537714  4C 8B 44 24 50                  mov r8, qword ptr [rsp + 0x50]
00537719  48 8D 96 80 00 00 00            lea rdx, [rsi + 0x80]
00537720  45 8B CE                        mov r9d, r14d
00537723  49 8B CF                        mov rcx, r15
00537726  8B D8                           mov ebx, eax
00537728  E8 A3 3D 00 00                  call 0x14053b4d0
0053772D  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00537732  F7 DB                           neg ebx
00537734  44 8B CB                        mov r9d, ebx
00537737  45 8B C6                        mov r8d, r14d
0053773A  49 8B D7                        mov rdx, r15
0053773D  E8 2E 3E 00 00                  call 0x14053b570
00537742  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00537747  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
0053774C  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
00537751  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
00537756  48 83 C4 20                     add rsp, 0x20
0053775A  41 5F                           pop r15
0053775C  C3                              ret
0053775D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptFdef369ModSubGeneric(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 32) = v_r14;
    v_rsp = (v_rsp) - (32);
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4))))) << (8));
    a3 = (unsigned int)((a3) + (64));
    result = EmpCheckErrataList(a5, a6, a3, a4);
    result = SymCryptFdef369RawSubAsm(a2, a3, a4, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)))));
    result = SymCryptFdef369RawAddAsm(a4, a1 + 128, a5, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)))));
    v_rbx = (unsigned int)(-((unsigned int)((unsigned int)(result))));
    result = SymCryptFdef369MaskedCopyAsm(a5, a4, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)))), (unsigned int)((unsigned int)(v_rbx)));
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptFdef369ModSubGeneric(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    *(uint64_t *)(local_rsp + 0x20) = local_r14;
    local_rsp = (local_rsp) - (32);
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4))))) << (8));
    Arg3 = (uint32_t)((Arg3) + (64));
    result = EmpCheckErrataList(Arg5, Arg6, Arg3, Arg4);
    result = SymCryptFdef369RawSubAsm(Arg2, Arg3, Arg4, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))));
    result = SymCryptFdef369RawAddAsm(Arg4, Arg1 + 128, Arg5, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))));
    local_rbx = (uint32_t)(-((uint32_t)((uint32_t)(result))));
    result = SymCryptFdef369MaskedCopyAsm(Arg5, Arg4, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))), (uint32_t)((uint32_t)(local_rbx)));
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x80` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005376C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005376C0[BB_005376C0]
  bb_0053775D[BB_0053775D]
```
