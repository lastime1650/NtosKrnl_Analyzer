# sub_006DDDE8

- RVA: `0x006DDDE8`–`0x006DDE00` (길이 `24` bytes)
- VA: `0x00000001406DDDE8`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000705C0`
- 디코드: `6`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006DDDEB` → [MiDecayNodeNowEmpty](../33/MiDecayNodeNowEmpty_function_0033C938.md) (function, `0x0033C938`)
- `0x006DDDF3` → [ExReleaseSpinLockSharedFromDpcLevel](../24/ExReleaseSpinLockSharedFromDpcLevel_function_0024A590.md) (function, `0x0024A590`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006DDDFB` → [MiEmptyDecayClusterTimers + 0x285](../2D/MiEmptyDecayClusterTimers_function_002DAB50.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006DDDE8  49 8B CF                        mov rcx, r15
006DDDEB  E8 48 EB C5 FF                  call 0x14033c938
006DDDF0  49 8B CE                        mov rcx, r14
006DDDF3  E8 98 C7 B6 FF                  call 0x14024a590
006DDDF8  48 8B EF                        mov rbp, rdi
006DDDFB  E9 D5 CF BF FF                  jmp 0x1402dadd5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006DDDE8(void)
{
    __int64 result;

    result = MiDecayNodeNowEmpty(v_r15, a2, a3, a4);
    result = ExReleaseSpinLockSharedFromDpcLevel(v_r14, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_006DDDE8(void)
{
    int64_t result;

    result = MiDecayNodeNowEmpty(local_r15, a2, a3, a4);
    result = ExReleaseSpinLockSharedFromDpcLevel(local_r14, a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006DDDE8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006DDDE8[BB_006DDDE8]
```
