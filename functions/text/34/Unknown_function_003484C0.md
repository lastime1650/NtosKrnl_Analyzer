# sub_003484C0

- RVA: `0x003484C0`–`0x003484CA` (길이 `10` bytes)
- VA: `0x00000001403484C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000781E0`
- 디코드: `3`개 명령, `10/10` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003484C3` → [ExAcquireSpinLockSharedAtDpcLevel](../24/ExAcquireSpinLockSharedAtDpcLevel_function_00248E30.md) (function, `0x00248E30`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x003484C8` → [sub_0034847F + 0x15](Unknown_function_0034847F.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003484C0  40 B5 11                        mov bpl, 0x11
003484C3  E8 68 09 F0 FF                  call 0x140248e30
003484C8  EB CA                           jmp 0x140348494
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_003484C0(void)
{
    __int64 result;

    result = ExAcquireSpinLockSharedAtDpcLevel(a1, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_003484C0(void)
{
    int64_t result;

    result = ExAcquireSpinLockSharedAtDpcLevel(a1, a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003484C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003484C0[BB_003484C0]
```
