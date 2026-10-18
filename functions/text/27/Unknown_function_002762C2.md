# sub_002762C2

- RVA: `0x002762C2`–`0x002762D6` (길이 `20` bytes)
- VA: `0x00000001402762C2`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00065EEC`
- 디코드: `5`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002762C5` → [MiUnlockPageTable](../21/MiUnlockPageTable_function_00216EC0.md) (function, `0x00216EC0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x002762D1` → [MiResolvePageTablePage + 0x8A](MiResolvePageTablePage_function_00275930.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002762C2  48 8B CD                        mov rcx, rbp
002762C5  E8 F6 0B FA FF                  call 0x140216ec0
002762CA  45 33 C9                        xor r9d, r9d
002762CD  4C 89 4E 10                     mov qword ptr [rsi + 0x10], r9
002762D1  E9 E4 F6 FF FF                  jmp 0x1402759ba
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002762C2(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;

    result = MiUnlockPageTable(v_rbp, a2, a3, a4);
    a4 = 0;
    *(unsigned __int64 *)(v_rsi + 16) = 0;
}
```

## 5. (Beta) C Style

```c
int64_t sub_002762C2(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;

    result = MiUnlockPageTable(local_rbp, Arg2, Arg3, Arg4);
    Arg4 = 0;
    *(uint64_t *)(local_rsi + 0x10) = 0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002762C2&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002762C2[BB_002762C2]
```
