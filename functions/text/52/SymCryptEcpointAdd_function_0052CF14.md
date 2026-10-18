# SymCryptEcpointAdd

- RVA: `0x0052CF14`–`0x0052CF5F` (길이 `75` bytes)
- VA: `0x000000014052CF14`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063458`
- 디코드: `19`개 명령, `75/75` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0052CF54` → `indirect target` (indirect, 간접 대상)

### Direct callers
- [SymCryptEcpointMultiScalarMulWnafWithInterleaving](SymCryptEcpointMultiScalarMulWnafWithInterleaving_function_0052B920.md) at `0x0052BD59`
- [SymCryptEcpointScalarMulFixedWindow](SymCryptEcpointScalarMulFixedWindow_function_0052BE30.md) at `0x0052C37C`

### Static image references
- `0x0052CF26` → RVA `0x00006CB0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0052CF14  48 83 EC 48                     sub rsp, 0x48
0052CF18  8B 41 04                        mov eax, dword ptr [rcx + 4]
0052CF1B  4D 8B D9                        mov r11, r9
0052CF1E  4C 8B 94 24 80 00 00 00         mov r10, qword ptr [rsp + 0x80]
0052CF26  4C 8D 0D 83 9D AD FF            lea r9, [rip - 0x52627d]
0052CF2D  4C 89 54 24 30                  mov qword ptr [rsp + 0x30], r10
0052CF32  83 E0 07                        and eax, 7
0052CF35  4C 8B 54 24 78                  mov r10, qword ptr [rsp + 0x78]
0052CF3A  48 C1 E0 07                     shl rax, 7
0052CF3E  4C 89 54 24 28                  mov qword ptr [rsp + 0x28], r10
0052CF43  4A 8B 04 08                     mov rax, qword ptr [rax + r9]
0052CF47  44 8B 4C 24 70                  mov r9d, dword ptr [rsp + 0x70]
0052CF4C  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
0052CF51  4D 8B CB                        mov r9, r11
0052CF54  FF D0                           call rax
0052CF56  0F 1F 00                        nop dword ptr [rax]
0052CF59  48 83 C4 48                     add rsp, 0x48
0052CF5D  C3                              ret
0052CF5E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptEcpointAdd(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, __int64 a6, __int64 a7)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m28;

    v_rsp = (v_rsp) - (72);
    v_stack_m18 = a7;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 4))) & (7));
    result = (result) << (7);
    v_stack_m20 = a6;
    v_stack_m28 = (unsigned int)((unsigned int)(a5));
    result = kernel_indirect_call(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptEcpointAdd(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, int64_t Arg6, int64_t Arg7)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint32_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    v_stack_m18 = Arg7;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x4))) & (7));
    result = (result) << (7);
    v_stack_m20 = Arg6;
    v_stack_m28 = (uint32_t)((uint32_t)(Arg5));
    result = kernel_indirect_call(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (72);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0052CF14&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0052CF14[BB_0052CF14]
  bb_0052CF5E[BB_0052CF5E]
```
