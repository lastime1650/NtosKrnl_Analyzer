# IovpSessionDataReference

- RVA: `0x00BAC870`–`0x00BAC882` (길이 `18` bytes)
- VA: `0x0000000140BAC870`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `7`개 명령, `18/18` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [IovpCallDriver1](../B9/IovpCallDriver1_function_00B9CCA4.md) at `0x00B9CE39`
- [IovpCallDriver1](../B9/IovpCallDriver1_function_00B9CCA4.md) at `0x00B9D20C`
- [sub_00BBBE00](../BB/Unknown_function_00BBBE00.md) at `0x00BBC098`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BAC870  83 79 08 00                     cmp dword ptr [rcx + 8], 0
00BAC874  75 07                           jne 0x140bac87d
00BAC876  48 8B 01                        mov rax, qword ptr [rcx]
00BAC879  F0 FF 40 14                     lock inc dword ptr [rax + 0x14]
00BAC87D  FF 41 08                        inc dword ptr [rcx + 8]
00BAC880  C3                              ret
00BAC881  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IovpSessionDataReference(__int64 a1)
{
    __int64 result;

    if ((*(unsigned int *)(a1 + 8)) == 0) {
        result = *(unsigned __int64 *)(a1);
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IovpSessionDataReference(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if ((*(uint32_t *)(arg1 + 0x8)) == 0) {
        result = *(uint64_t *)(arg1);
    }
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BAC870&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BAC870[BB_00BAC870]
  bb_00BAC876[BB_00BAC876]
  bb_00BAC87D[BB_00BAC87D]
  bb_00BAC881[BB_00BAC881]
  bb_00BAC870 -->|branch| bb_00BAC87D
  bb_00BAC870 -->|fallthrough| bb_00BAC876
  bb_00BAC876 -->|flow| bb_00BAC87D
```
