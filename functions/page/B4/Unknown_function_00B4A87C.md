# sub_00B4A87C

- RVA: `0x00B4A87C`–`0x00B4A88A` (길이 `14` bytes)
- VA: `0x0000000140B4A87C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BC3CC`
- 디코드: `4`개 명령, `14/14` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B4A87F` → [IoFreeIrp](../../text/24/IoFreeIrp_function_0024DF70.md) (function, `0x0024DF70`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B4A87F` → [IoFreeIrp](../../text/24/IoFreeIrp_function_0024DF70.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00B4A885` → [WmipGetFilePDO + 0x6E](../AA/WmipGetFilePDO_function_00AAF454.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B4A87C  48 8B CF                        mov rcx, rdi
00B4A87F  E8 EC 36 70 FF                  call 0x14024df70
00B4A884  90                              nop
00B4A885  E9 38 4C F6 FF                  jmp 0x140aaf4c2
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B4A87C(void)
{
    __int64 result;

    result = IoFreeIrp(v_rdi, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_00B4A87C(void)
{
    int64_t result;

    result = IoFreeIrp(local_rdi, a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B4A87C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B4A87C[BB_00B4A87C]
```
