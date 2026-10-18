# sub_0037DE20

- RVA: `0x0037DE20`–`0x0037DE34` (길이 `20` bytes)
- VA: `0x000000014037DE20`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007B62C`
- 디코드: `6`개 명령, `20/20` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0037DE2F` → [sub_0037DCAF + 0x36](Unknown_function_0037DCAF.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0037DE20  41 8B 0A                        mov ecx, dword ptr [r10]
0037DE23  0F 33                           rdpmc
0037DE25  48 C1 E2 20                     shl rdx, 0x20
0037DE29  48 0B C2                        or rax, rdx
0037DE2C  49 89 03                        mov qword ptr [r11], rax
0037DE2F  E9 B1 FE FF FF                  jmp 0x14037dce5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0037DE20(__int64 a1, __int64 a2)
{
    __int64 result;

    a2 = (a2) << (32);
    result = (result) | (a2);
    *(unsigned __int64 *)(v_r11) = result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_0037DE20(int64_t Arg1, int64_t Arg2)
{
    int64_t result;

    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    *(uint64_t *)(local_r11) = result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0037DE20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0037DE20[BB_0037DE20]
```
