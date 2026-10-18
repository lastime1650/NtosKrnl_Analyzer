# sub_00207BA7

- RVA: `0x00207BA7`–`0x00207BC1` (길이 `26` bytes)
- VA: `0x0000000140207BA7`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2A0`
- 디코드: `5`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00207BBA` → [KxWaitForSpinLockAndAcquire](KxWaitForSpinLockAndAcquire_function_002085C0.md) (function, `0x002085C0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00207BB1` → [sub_00207B41 + 0x3E](Unknown_function_00207B41.md) (`tail-transfer`)
  - `0x00207BBF` → [sub_00207B41 + 0x3E](Unknown_function_00207B41.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00207BA7  F0 48 0F BA AB 18 06 00 00 00   lock bts qword ptr [rbx + 0x618], 0
00207BB1  73 CC                           jae 0x140207b7f
00207BB3  48 8D 8B 18 06 00 00            lea rcx, [rbx + 0x618]
00207BBA  E8 01 0A 00 00                  call 0x1402085c0
00207BBF  EB BE                           jmp 0x140207b7f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00207BA7(void)
{
    __int64 result;

    result = KxWaitForSpinLockAndAcquire(v_rbx + 1560, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_00207BA7(void)
{
    int64_t result;

    result = KxWaitForSpinLockAndAcquire(local_rbx + 1560, a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00207BA7&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00207BA7[BB_00207BA7]
  bb_00207BB3[BB_00207BB3]
  bb_00207BA7 -->|fallthrough| bb_00207BB3
```
