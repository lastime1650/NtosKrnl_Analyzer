# sub_00312B1E

- RVA: `0x00312B1E`–`0x00312B2B` (길이 `13` bytes)
- VA: `0x0000000140312B1E`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00074394`
- 디코드: `3`개 명령, `13/13` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00312B21` → [KeFlushTb](KeFlushTb_function_00314140.md) (function, `0x00314140`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00312B26` → [sub_003121DC](Unknown_function_003121DC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00312B1E  41 8B D1                        mov edx, r9d
00312B21  E8 1A 16 00 00                  call 0x140314140
00312B26  E9 B1 F6 FF FF                  jmp 0x1403121dc
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00312B1E(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;

    result = KeFlushTb(a1, (unsigned int)(a4), a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_00312B1E(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;

    result = KeFlushTb(Arg1, (uint32_t)(Arg4), Arg3, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00312B1E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00312B1E[BB_00312B1E]
```
