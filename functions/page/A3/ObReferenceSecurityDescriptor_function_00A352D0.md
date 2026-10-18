# ObReferenceSecurityDescriptor

- RVA: `0x00A352D0`–`0x00A352E8` (길이 `24` bytes)
- VA: `0x0000000140A352D0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A352D0  8B C2                           mov eax, edx
00A352D2  F0 48 0F C1 41 E8               lock xadd qword ptr [rcx - 0x18], rax
00A352D8  48 85 C0                        test rax, rax
00A352DB  7E 02                           jle 0x140a352df
00A352DD  C3                              ret
00A352DE  CC                              int3
00A352DF  B9 0E 00 00 00                  mov ecx, 0xe
00A352E4  CD 29                           int 0x29
00A352E6  C3                              ret
00A352E7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObReferenceSecurityDescriptor(__int64 a1, int a2)
{
    if (condition_is_less_or_equal) goto loc_00A352DF;
    return (unsigned int)(a2);
loc_00A352DF:
    return (unsigned int)(a2);
}
```

## 5. (Beta) C Style

```c
int64_t ObReferenceSecurityDescriptor(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    if (condition_is_less_or_equal) goto loc_00A352DF;
    return (uint32_t)(Arg2);
loc_00A352DF:
    return (uint32_t)(Arg2);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x18` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A352D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A352D0[BB_00A352D0]
  bb_00A352DD[BB_00A352DD]
  bb_00A352DE[BB_00A352DE]
  bb_00A352DF[BB_00A352DF]
  bb_00A352E7[BB_00A352E7]
  bb_00A352D0 -->|branch| bb_00A352DF
  bb_00A352D0 -->|fallthrough| bb_00A352DD
  bb_00A352DE -->|flow| bb_00A352DF
```
