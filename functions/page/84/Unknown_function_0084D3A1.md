# sub_0084D3A1

- RVA: `0x0084D3A1`–`0x0084D3C7` (길이 `38` bytes)
- VA: `0x000000014084D3A1`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006990C`
- 디코드: `10`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0084D3A8` → [CmpConstructNameFromKcbNameBlocks](CmpConstructNameFromKcbNameBlocks_function_0084D510.md) (function, `0x0084D510`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x0084D3B1` → [sub_0084D18D + 0x137](Unknown_function_0084D18D.md) (`tail-transfer`)
  - `0x0084D3BA` → [sub_0084D18D + 0x13D](Unknown_function_0084D18D.md) (`tail-transfer`)
  - `0x0084D3C2` → [sub_0084D18D + 0xDC](Unknown_function_0084D18D.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0084D3A1  48 8D 55 9F                     lea rdx, [rbp - 0x61]
0084D3A5  48 8B CF                        mov rcx, rdi
0084D3A8  E8 63 01 00 00                  call 0x14084d510
0084D3AD  8B F8                           mov edi, eax
0084D3AF  85 C0                           test eax, eax
0084D3B1  0F 89 0D FF FF FF               jns 0x14084d2c4
0084D3B7  4C 8B FB                        mov r15, rbx
0084D3BA  E9 0B FF FF FF                  jmp 0x14084d2ca
0084D3BF  66 FF C9                        dec cx
0084D3C2  E9 A2 FE FF FF                  jmp 0x14084d269
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0084D3A1(void)
{
    __int64 result;

    result = CmpConstructNameFromKcbNameBlocks(v_rdi, v_rbp - 97, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_0084D3A1(void)
{
    int64_t result;

    result = CmpConstructNameFromKcbNameBlocks(local_rdi, local_rbp - 97, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0084D3A1&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0084D3A1[BB_0084D3A1]
  bb_0084D3B7[BB_0084D3B7]
  bb_0084D3BF[BB_0084D3BF]
  bb_0084D3A1 -->|fallthrough| bb_0084D3B7
```
