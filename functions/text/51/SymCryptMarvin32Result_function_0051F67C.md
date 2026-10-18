# SymCryptMarvin32Result

- RVA: `0x0051F67C`–`0x0051F6E1` (길이 `101` bytes)
- VA: `0x000000014051F67C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BC4`
- 디코드: `30`개 명령, `101/101` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0051F6AF` → [SymCryptMarvin32AppendBlocks](SymCryptMarvin32AppendBlocks_function_0051F570.md) (function, `0x0051F570`)

### Direct callers
- [HvpGenerateLogEntryChecksums](../../page/9B/HvpGenerateLogEntryChecksums_function_009B6A5C.md) at `0x009B6AF0`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0051F67C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0051F681  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0051F686  57                              push rdi
0051F687  48 83 EC 20                     sub rsp, 0x20
0051F68B  8B 41 28                        mov eax, dword ptr [rcx + 0x28]
0051F68E  48 8D 59 10                     lea rbx, [rcx + 0x10]
0051F692  83 E0 03                        and eax, 3
0051F695  48 8B FA                        mov rdi, rdx
0051F698  48 8B F1                        mov rsi, rcx
0051F69B  48 8B D1                        mov rdx, rcx
0051F69E  41 B8 08 00 00 00               mov r8d, 8
0051F6A4  83 24 08 00                     and dword ptr [rax + rcx], 0
0051F6A8  C6 04 08 80                     mov byte ptr [rax + rcx], 0x80
0051F6AC  48 8B CB                        mov rcx, rbx
0051F6AF  E8 BC FE FF FF                  call 0x14051f570
0051F6B4  8B 03                           mov eax, dword ptr [rbx]
0051F6B6  89 07                           mov dword ptr [rdi], eax
0051F6B8  8B 46 14                        mov eax, dword ptr [rsi + 0x14]
0051F6BB  89 47 04                        mov dword ptr [rdi + 4], eax
0051F6BE  83 26 00                        and dword ptr [rsi], 0
0051F6C1  48 8B 46 20                     mov rax, qword ptr [rsi + 0x20]
0051F6C5  83 66 28 00                     and dword ptr [rsi + 0x28], 0
0051F6C9  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
0051F6CE  0F 28 00                        movaps xmm0, xmmword ptr [rax]
0051F6D1  F3 0F 7F 03                     movdqu xmmword ptr [rbx], xmm0
0051F6D5  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0051F6DA  48 83 C4 20                     add rsp, 0x20
0051F6DE  5F                              pop rdi
0051F6DF  C3                              ret
0051F6E0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptMarvin32Result(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 40))) & (3));
    *(unsigned __int8 *)(result + a1 * 1) = 128;
    result = SymCryptMarvin32AppendBlocks(a1 + 16, a1, 8, a4);
    *(unsigned int *)(a2) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16)));
    *(unsigned int *)(a2 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 20)));
    *(unsigned __int64 *)(a1 + 16) = v_xmm0;
    v_rsp = (v_rsp) + (32);
    return *(unsigned __int64 *)(a1 + 32);
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptMarvin32Result(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x28))) & (3));
    *(uint8_t *)(result + arg1 * 1) = 128;
    result = SymCryptMarvin32AppendBlocks(Arg1 + 16, Arg1, 8, a4);
    *(uint32_t *)(arg2) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    *(uint32_t *)(arg2 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x14)));
    *(uint64_t *)(arg1 + 0x10) = v_xmm0;
    local_rsp = (local_rsp) + (32);
    return *(uint64_t *)(arg1 + 0x20);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x0` | `128` | `W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x14` | `32` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R/W` |
| `Arg2` | `+ 0x0` | `32` | `W` |
| `Arg2` | `+ 0x4` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0051F67C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0051F67C[BB_0051F67C]
  bb_0051F6E0[BB_0051F6E0]
```
