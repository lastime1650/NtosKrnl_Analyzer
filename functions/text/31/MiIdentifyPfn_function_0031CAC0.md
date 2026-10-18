# MiIdentifyPfn

- RVA: `0x0031CAC0`–`0x0031CB02` (길이 `66` bytes)
- VA: `0x000000014031CAC0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00074E64`
- 디코드: `18`개 명령, `66/66` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **10**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiDemoteCombinedPte](../22/MiDemoteCombinedPte_function_0022ABAC.md) at `0x0022AFCC`
- [MiCombineWithExisting](../22/MiCombineWithExisting_function_0022B4B8.md) at `0x0022B712`
- [MiCombineInitialInstance](../22/MiCombineInitialInstance_function_0022BC0C.md) at `0x0022CA14`
- [MiMakePageAvoidRead](../2B/MiMakePageAvoidRead_function_002B7DE0.md) at `0x002B84CA`
- [sub_0031C992](Unknown_function_0031C992.md) at `0x0031C998`
- [MmSetPfnListInfo](MmSetPfnListInfo_function_0031D61C.md) at `0x0031D70B`
- [MiCopyOnWrite](../36/MiCopyOnWrite_function_00362A0C.md) at `0x00363543`
- [MiDecommitPrivatePageTail](../36/MiDecommitPrivatePageTail_function_0036F564.md) at `0x0036F83E`
- [MmTryIdentifyPage](../67/MmTryIdentifyPage_function_00678738.md) at `0x006787E8`
- [MiUpdateBadPfnIdentity](../67/MiUpdateBadPfnIdentity_function_0067A890.md) at `0x0067A959`

### Static image references
- `0x0031CAE6` → RVA `0x00E300B8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0031CAFC` → [sub_0031D4A9 + 0x3F](Unknown_function_0031D4A9.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0031CAC0  40 55                           push rbp
0031CAC2  56                              push rsi
0031CAC3  41 56                           push r14
0031CAC5  48 8D 6C 24 B9                  lea rbp, [rsp - 0x47]
0031CACA  48 81 EC 90 00 00 00            sub rsp, 0x90
0031CAD1  33 C0                           xor eax, eax
0031CAD3  0F 57 C0                        xorps xmm0, xmm0
0031CAD6  0F 57 C9                        xorps xmm1, xmm1
0031CAD9  48 8B F2                        mov rsi, rdx
0031CADC  0F 11 0A                        movups xmmword ptr [rdx], xmm1
0031CADF  48 89 42 10                     mov qword ptr [rdx + 0x10], rax
0031CAE3  4C 8B F1                        mov r14, rcx
0031CAE6  48 8B 05 CB 35 B1 00            mov rax, qword ptr [rip + 0xb135cb]
0031CAED  0F 11 45 EF                     movups xmmword ptr [rbp - 0x11], xmm0
0031CAF1  0F 11 45 FF                     movups xmmword ptr [rbp - 1], xmm0
0031CAF5  0F 11 45 0F                     movups xmmword ptr [rbp + 0xf], xmm0
0031CAF9  48 85 C0                        test rax, rax
0031CAFC  0F 85 E6 09 00 00               jne 0x14031d4e8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiIdentifyPfn(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m70;

    v_rsp = (v_rsp) - (144);
    result = 0;
    *(unsigned __int64 *)(a2) = v_xmm1;
    *(unsigned __int64 *)(a2 + 16) = 0;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
}
```

## 5. (Beta) C Style

```c
int64_t MiIdentifyPfn(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m70;

    local_rsp = (local_rsp) - (144);
    result = 0;
    *(uint64_t *)(arg2) = v_xmm1;
    *(uint64_t *)(arg2 + 0x10) = 0;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `128` | `R` |
| `Arg2` | `+ 0x10` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0031CAC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0031CAC0[BB_0031CAC0]
```
