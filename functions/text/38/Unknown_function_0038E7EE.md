# sub_0038E7EE

- RVA: `0x0038E7EE`–`0x0038E800` (길이 `18` bytes)
- VA: `0x000000014038E7EE`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00080680`
- 디코드: `6`개 명령, `18/18` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0038E7F6` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0038E7FE` → [sub_0038E7A7 + 0x2E](Unknown_function_0038E7A7.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0038E7EE  4C 8B C5                        mov r8, rbp
0038E7F1  33 D2                           xor edx, edx
0038E7F3  48 8B CE                        mov rcx, rsi
0038E7F6  E8 45 84 33 00                  call 0x1406c6c40
0038E7FB  48 03 F5                        add rsi, rbp
0038E7FE  EB D5                           jmp 0x14038e7d5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0038E7EE(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsi;

    a2 = 0;
    result = memset(v_rsi, a2, v_rbp, a4);
    v_rsi = (v_rsi) + (v_rbp);
}
```

## 5. (Beta) C Style

```c
int64_t sub_0038E7EE(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsi;

    Arg2 = 0;
    result = memset(local_rsi, Arg2, local_rbp, a4);
    local_rsi = (local_rsi) + (local_rbp);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0038E7EE&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0038E7EE[BB_0038E7EE]
```
