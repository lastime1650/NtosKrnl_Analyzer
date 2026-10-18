# sub_006DDD38

- RVA: `0x006DDD38`–`0x006DDD49` (길이 `17` bytes)
- VA: `0x00000001406DDD38`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00070288`
- 디코드: `5`개 명령, `17/17` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006DDD3E` → [MiPruneCachedStackList](../49/MiPruneCachedStackList_function_00495638.md) (function, `0x00495638`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006DDD44` → [MiAdjustCachedStacks + 0xC5](../2D/MiAdjustCachedStacks_function_002D8AAC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006DDD38  45 33 C0                        xor r8d, r8d
006DDD3B  48 8B CE                        mov rcx, rsi
006DDD3E  E8 F5 78 DB FF                  call 0x140495638
006DDD43  90                              nop
006DDD44  E9 28 AE BF FF                  jmp 0x1402d8b71
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006DDD38(__int64 a1, __int64 a2, int a3)
{
    __int64 result;

    a3 = 0;
    result = MiPruneCachedStackList(v_rsi, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_006DDD38(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;

    Arg3 = 0;
    result = MiPruneCachedStackList(local_rsi, Arg2, Arg3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006DDD38&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006DDD38[BB_006DDD38]
```
