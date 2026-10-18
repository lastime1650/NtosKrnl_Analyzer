# sub_00B2DE30

- RVA: `0x00B2DE30`–`0x00B2DE44` (길이 `20` bytes)
- VA: `0x0000000140B2DE30`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009E7CC`
- 디코드: `6`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B2DE39` → [CmpDoFileSetSizeEx](../9B/CmpDoFileSetSizeEx_function_009B2A4C.md) (function, `0x009B2A4C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00B2DE3F` → [HvTruncateAllLogFilesIfRequired + 0x37](../9B/HvTruncateAllLogFilesIfRequired_function_009B6E1C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B2DE30  45 33 C9                        xor r9d, r9d
00B2DE33  45 33 C0                        xor r8d, r8d
00B2DE36  48 8B CB                        mov rcx, rbx
00B2DE39  E8 0E 4C E8 FF                  call 0x1409b2a4c
00B2DE3E  90                              nop
00B2DE3F  E9 0F 90 E8 FF                  jmp 0x1409b6e53
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B2DE30(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;

    a4 = 0;
    a3 = 0;
    result = CmpDoFileSetSizeEx(v_rbx, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B2DE30(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;

    Arg4 = 0;
    Arg3 = 0;
    result = CmpDoFileSetSizeEx(local_rbx, Arg2, Arg3, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B2DE30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B2DE30[BB_00B2DE30]
```
