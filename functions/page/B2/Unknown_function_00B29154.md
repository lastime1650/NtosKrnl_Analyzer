# sub_00B29154

- RVA: `0x00B29154`–`0x00B29175` (길이 `33` bytes)
- VA: `0x0000000140B29154`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000960E4`
- 디코드: `9`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B2916A` → [SepFreeCapturedTokenSecurityAttributesInformation](../A4/SepFreeCapturedTokenSecurityAttributesInformation_function_00A4D124.md) (function, `0x00A4D124`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x00B29159` → [SepCaptureTokenSecurityAttributesAndOperationsInformation + 0x156](../97/SepCaptureTokenSecurityAttributesAndOperationsInformation_function_00971E0C.md) (`tail-transfer`)
  - `0x00B29161` → [SepCaptureTokenSecurityAttributesAndOperationsInformation + 0x154](../97/SepCaptureTokenSecurityAttributesAndOperationsInformation_function_00971E0C.md) (`tail-transfer`)
  - `0x00B29170` → [SepCaptureTokenSecurityAttributesAndOperationsInformation + 0x154](../97/SepCaptureTokenSecurityAttributesAndOperationsInformation_function_00971E0C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B29154  49 89 08                        mov qword ptr [r8], rcx
00B29157  33 C0                           xor eax, eax
00B29159  E9 04 8E E4 FF                  jmp 0x140971f62
00B2915E  48 85 DB                        test rbx, rbx
00B29161  0F 84 F9 8D E4 FF               je 0x140971f60
00B29167  48 8B CB                        mov rcx, rbx
00B2916A  E8 B5 3F F2 FF                  call 0x140a4d124
00B2916F  90                              nop
00B29170  E9 EB 8D E4 FF                  jmp 0x140971f60
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B29154(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;

    *(unsigned __int64 *)(a3) = a1;
    result = 0;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B29154(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;

    *(uint64_t *)(arg3) = Arg1;
    result = 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B29154&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B29154[BB_00B29154]
  bb_00B2915E[BB_00B2915E]
  bb_00B29167[BB_00B29167]
  bb_00B2915E -->|fallthrough| bb_00B29167
```
