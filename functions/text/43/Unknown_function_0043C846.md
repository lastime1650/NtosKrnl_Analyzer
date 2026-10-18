# sub_0043C846

- RVA: `0x0043C846`–`0x0043C86B` (길이 `37` bytes)
- VA: `0x000000014043C846`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A459C`
- 디코드: `8`개 명령, `37/37` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0043C859` → [sub_0043C86B](Unknown_function_0043C86B.md) (`tail-transfer`)
  - `0x0043C866` → [KiSrcuCheckQuiescent + 0x13](KiSrcuCheckQuiescent_function_0043C700.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0043C846  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
0043C84F  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
0043C856  4D 85 C0                        test r8, r8
0043C859  75 10                           jne 0x14043c86b
0043C85B  FB                              sti
0043C85C  48 8B 74 24 30                  mov rsi, qword ptr [rsp + 0x30]
0043C861  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0043C866  E9 A8 FE FF FF                  jmp 0x14043c713
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_0043C846(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7)
{
}
```

## 5. (Beta) C Style

```c
void sub_0043C846(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, int64_t Arg6, int64_t Arg7)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0043C846&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0043C846[BB_0043C846]
  bb_0043C85B[BB_0043C85B]
  bb_0043C846 -->|fallthrough| bb_0043C85B
```
