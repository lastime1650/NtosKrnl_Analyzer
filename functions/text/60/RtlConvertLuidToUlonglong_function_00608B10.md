# RtlConvertLuidToUlonglong

- RVA: `0x00608B10`–`0x00608B24` (길이 `20` bytes)
- VA: `0x0000000140608B10`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `7`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [SepLogTokenSidManagement](../../page/79/SepLogTokenSidManagement_function_0079DA10.md) at `0x0079DA90`
- [SepLogTokenSidManagement](../../page/79/SepLogTokenSidManagement_function_0079DA10.md) at `0x0079DA9E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00608B10  8B 01                           mov eax, dword ptr [rcx]
00608B12  89 44 24 08                     mov dword ptr [rsp + 8], eax
00608B16  8B 41 04                        mov eax, dword ptr [rcx + 4]
00608B19  89 44 24 0C                     mov dword ptr [rsp + 0xc], eax
00608B1D  48 8B 44 24 08                  mov rax, qword ptr [rsp + 8]
00608B22  C3                              ret
00608B23  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlConvertLuidToUlonglong(__int64 a1)
{
    unsigned int v_stack_p8;
    unsigned int v_stack_pC;

    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    v_stack_pC = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)));
    return v_stack_p8;
}
```

## 5. (Beta) C Style

```c
int64_t RtlConvertLuidToUlonglong(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    uint32_t v_stack_p8;
    uint32_t v_stack_pC;

    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1)));
    v_stack_pC = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)));
    return v_stack_p8;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00608B10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00608B10[BB_00608B10]
  bb_00608B23[BB_00608B23]
```
