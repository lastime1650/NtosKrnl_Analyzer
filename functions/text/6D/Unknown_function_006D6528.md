# sub_006D6528

- RVA: `0x006D6528`–`0x006D653A` (길이 `18` bytes)
- VA: `0x00000001406D6528`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C9EC`
- 디코드: `5`개 명령, `18/18` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006D652F` → [KiReleaseThreadLockLowerIrql](../3C/KiReleaseThreadLockLowerIrql_function_003C65D0.md) (function, `0x003C65D0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006D6535` → [KiSchedulerApc + 0x71](../20/KiSchedulerApc_function_00202BC0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006D6528  8A 54 24 30                     mov dl, byte ptr [rsp + 0x30]
006D652C  48 8B CB                        mov rcx, rbx
006D652F  E8 9C 00 CF FF                  call 0x1403c65d0
006D6534  90                              nop
006D6535  E9 F7 C6 B2 FF                  jmp 0x140202c31
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006D6528(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned __int8 a6)
{
    __int64 result;

    result = KiReleaseThreadLockLowerIrql(v_rbx, a6, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_006D6528(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint8_t Arg6)
{
    int64_t result;

    result = KiReleaseThreadLockLowerIrql(local_rbx, Arg6, Arg3, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D6528&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D6528[BB_006D6528]
```
