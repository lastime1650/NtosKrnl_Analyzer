# sub_006F9C7C

- RVA: `0x006F9C7C`–`0x006F9C99` (길이 `29` bytes)
- VA: `0x00000001406F9C7C`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B7568`
- 디코드: `7`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006F9C7C` → [VfTargetDriversGetNode](../3E/VfTargetDriversGetNode_function_003EE174.md) (function, `0x003EE174`)
- `0x006F9C8D` → [ViDifCaptureIoCallbacks](../../pagevrfy/B9/ViDifCaptureIoCallbacks_function_00B9A748.md) (function, `0x00B9A748`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x006F9C8D` → [ViDifCaptureIoCallbacks](../../pagevrfy/B9/ViDifCaptureIoCallbacks_function_00B9A748.md) (`.text` → `PAGEVRFY`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x006F9C84` → [VfDifCaptureIoCallbacks + 0x1B](../4A/VfDifCaptureIoCallbacks_function_004A8698.md) (`tail-transfer`)
  - `0x006F9C94` → [VfDifCaptureIoCallbacks + 0x1D](../4A/VfDifCaptureIoCallbacks_function_004A8698.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006F9C7C  E8 F3 44 CF FF                  call 0x1403ee174
006F9C81  48 85 C0                        test rax, rax
006F9C84  0F 84 29 EA DA FF               je 0x1404a86b3
006F9C8A  48 8B CB                        mov rcx, rbx
006F9C8D  E8 B6 0A 4A 00                  call 0x140b9a748
006F9C92  B0 01                           mov al, 1
006F9C94  E9 1C EA DA FF                  jmp 0x1404a86b5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006F9C7C(void)
{
    __int64 result;

    result = VfTargetDriversGetNode(a1, a2, a3, a4);
    result = ViDifCaptureIoCallbacks(v_rbx, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_006F9C7C(void)
{
    int64_t result;

    result = VfTargetDriversGetNode(a1, a2, a3, a4);
    result = ViDifCaptureIoCallbacks(local_rbx, a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006F9C7C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006F9C7C[BB_006F9C7C]
  bb_006F9C8A[BB_006F9C8A]
  bb_006F9C7C -->|fallthrough| bb_006F9C8A
```
