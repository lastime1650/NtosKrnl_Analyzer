# sub_0042ACFF

- RVA: `0x0042ACFF`–`0x0042AD14` (길이 `21` bytes)
- VA: `0x000000014042ACFF`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A1294`
- 디코드: `7`개 명령, `21/21` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0042AD0A` → [MiLockVadCore](../29/MiLockVadCore_function_00297170.md) (function, `0x00297170`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0042AD12` → [sub_0042AC9A + 0x1C](Unknown_function_0042AC9A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0042ACFF  44 0F 20 C0                     mov rax, cr8
0042AD03  33 D2                           xor edx, edx
0042AD05  3C 02                           cmp al, 2
0042AD07  0F 94 C2                        sete dl
0042AD0A  E8 61 C4 E6 FF                  call 0x140297170
0042AD0F  0F B6 F0                        movzx esi, al
0042AD12  EB A2                           jmp 0x14042acb6
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0042ACFF(__int64 a1, int a2)
{
    __int64 result;

    a2 = 0;
    a2 = (((unsigned __int8)(v_cr8)) == 2) ? 1 : 0;
    result = MiLockVadCore(a1, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_0042ACFF(int64_t Arg1, int32_t Arg2)
{
    int64_t result;

    Arg2 = 0;
    Arg2 = (((uint8_t)(v_cr8)) == 2) ? 1 : 0;
    result = MiLockVadCore(Arg1, Arg2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0042ACFF&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0042ACFF[BB_0042ACFF]
```
