# SymCryptEcpointMultiScalarMul

- RVA: `0x0052D054`–`0x0052D0B3` (길이 `95` bytes)
- VA: `0x000000014052D054`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000697A4`
- 디코드: `25`개 명령, `95/95` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0052D0A7` → `indirect target` (indirect, 간접 대상)

### Direct callers
- [SymCryptEcDsaVerify](SymCryptEcDsaVerify_function_00526400.md) at `0x005268BE`

### Static image references
- `0x0052D068` → RVA `0x00006CD8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0052D054  40 53                           push rbx
0052D056  48 83 EC 40                     sub rsp, 0x40
0052D05A  8B 41 04                        mov eax, dword ptr [rcx + 4]
0052D05D  48 8B DA                        mov rbx, rdx
0052D060  4C 8B 94 24 88 00 00 00         mov r10, qword ptr [rsp + 0x88]
0052D068  48 8D 15 69 9C AD FF            lea rdx, [rip - 0x526397]
0052D06F  4C 89 54 24 38                  mov qword ptr [rsp + 0x38], r10
0052D074  83 E0 07                        and eax, 7
0052D077  4C 8B 94 24 80 00 00 00         mov r10, qword ptr [rsp + 0x80]
0052D07F  45 8B D9                        mov r11d, r9d
0052D082  4C 8B 4C 24 78                  mov r9, qword ptr [rsp + 0x78]
0052D087  4C 89 54 24 30                  mov qword ptr [rsp + 0x30], r10
0052D08C  4C 89 4C 24 28                  mov qword ptr [rsp + 0x28], r9
0052D091  45 8B CB                        mov r9d, r11d
0052D094  48 C1 E0 07                     shl rax, 7
0052D098  48 8B 04 10                     mov rax, qword ptr [rax + rdx]
0052D09C  8B 54 24 70                     mov edx, dword ptr [rsp + 0x70]
0052D0A0  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
0052D0A4  48 8B D3                        mov rdx, rbx
0052D0A7  FF D0                           call rax
0052D0A9  0F 1F 00                        nop dword ptr [rax]
0052D0AC  48 83 C4 40                     add rsp, 0x40
0052D0B0  5B                              pop rbx
0052D0B1  C3                              ret
0052D0B2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptEcpointMultiScalarMul(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned int a5, __int64 a6, __int64 a7, __int64 a8)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m28;

    v_rsp = (v_rsp) - (64);
    v_stack_m10 = a8;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 4))) & (7));
    v_stack_m18 = a7;
    v_stack_m20 = a6;
    result = (result) << (7);
    v_stack_m28 = (unsigned int)((unsigned int)(a5));
    result = kernel_indirect_call(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptEcpointMultiScalarMul(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint32_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint32_t v_stack_m28;

    local_rsp = (local_rsp) - (64);
    v_stack_m10 = Arg8;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x4))) & (7));
    v_stack_m18 = Arg7;
    v_stack_m20 = Arg6;
    result = (result) << (7);
    v_stack_m28 = (uint32_t)((uint32_t)(Arg5));
    result = kernel_indirect_call(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    local_rsp = (local_rsp) + (64);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0052D054&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0052D054[BB_0052D054]
  bb_0052D0B2[BB_0052D0B2]
```
