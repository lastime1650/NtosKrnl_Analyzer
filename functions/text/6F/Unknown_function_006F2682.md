# sub_006F2682

- RVA: `0x006F2682`–`0x006F2696` (길이 `20` bytes)
- VA: `0x00000001406F2682`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A9F64`
- 디코드: `4`개 명령, `20/20` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x006F2689` → [RtlStringCbPrintfExW + 0x52](../46/RtlStringCbPrintfExW_function_00461AD4.md) (`tail-transfer`)
  - `0x006F2691` → [RtlStringCbPrintfExW + 0x52](../46/RtlStringCbPrintfExW_function_00461AD4.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006F2682  48 81 FF FF FF FF 7F            cmp rdi, 0x7fffffff
006F2689  0F 86 97 F4 D6 FF               jbe 0x140461b26
006F268F  8B DA                           mov ebx, edx
006F2691  E9 90 F4 D6 FF                  jmp 0x140461b26
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_006F2682(__int64 a1, int a2)
{
}
```

## 5. (Beta) C Style

```c
void sub_006F2682(int64_t Arg1, int32_t Arg2)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006F2682&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006F2682[BB_006F2682]
  bb_006F268F[BB_006F268F]
  bb_006F2682 -->|fallthrough| bb_006F268F
```
