# SymCryptEcurveFillScratchSpaces

- RVA: `0x0052D1D0`–`0x0052D1F4` (길이 `36` bytes)
- VA: `0x000000014052D1D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `11`개 명령, `36/36` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0052D1E9` → `indirect target` (indirect, 간접 대상)

### Direct callers
- [SymCryptEcurveInitialize](SymCryptEcurveInitialize_function_005241A4.md) at `0x00524529`

### Static image references
- `0x0052D1D7` → RVA `0x00006CE0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0052D1D0  48 83 EC 28                     sub rsp, 0x28
0052D1D4  8B 41 04                        mov eax, dword ptr [rcx + 4]
0052D1D7  48 8D 15 02 9B AD FF            lea rdx, [rip - 0x5264fe]
0052D1DE  83 E0 07                        and eax, 7
0052D1E1  48 C1 E0 07                     shl rax, 7
0052D1E5  48 8B 04 10                     mov rax, qword ptr [rax + rdx]
0052D1E9  FF D0                           call rax
0052D1EB  0F 1F 00                        nop dword ptr [rax]
0052D1EE  48 83 C4 28                     add rsp, 0x28
0052D1F2  C3                              ret
0052D1F3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptEcurveFillScratchSpaces(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 4))) & (7));
    result = (result) << (7);
    result = kernel_indirect_call(a1, v_rip - 5399806, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptEcurveFillScratchSpaces(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x4))) & (7));
    result = (result) << (7);
    result = kernel_indirect_call(Arg1, v_rip - 5399806, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0052D1D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0052D1D0[BB_0052D1D0]
  bb_0052D1F3[BB_0052D1F3]
```
