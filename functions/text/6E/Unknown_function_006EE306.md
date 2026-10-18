# sub_006EE306

- RVA: `0x006EE306`–`0x006EE317` (길이 `17` bytes)
- VA: `0x00000001406EE306`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A12C8`
- 디코드: `5`개 명령, `17/17` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006EE30C` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006EE312` → [MiDeprioritizeVirtualAddresses + 0x94](../42/MiDeprioritizeVirtualAddresses_function_0042AD1C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006EE306  49 8B D7                        mov rdx, r15
006EE309  48 8B CD                        mov rcx, rbp
006EE30C  E8 AF 8B B2 FF                  call 0x140216ec0
006EE311  90                              nop
006EE312  E9 99 CA D3 FF                  jmp 0x14042adb0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006EE306(void)
{
    __int64 result;

    result = MiUnlockPageTable(v_rbp, v_r15, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_006EE306(void)
{
    int64_t result;

    result = MiUnlockPageTable(local_rbp, local_r15, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006EE306&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006EE306[BB_006EE306]
```
