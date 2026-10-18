# sub_003563AB

- RVA: `0x003563AB`–`0x003563CB` (길이 `32` bytes)
- VA: `0x00000001403563AB`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00079444`
- 디코드: `8`개 명령, `32/32` bytes 표시
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
  - `0x003563B9` → [sub_00356427](Unknown_function_00356427.md) (`tail-transfer`)
  - `0x003563C9` → [sub_003563CB + 0xC](Unknown_function_003563CB.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003563AB  48 8B 87 B8 8E 00 00            mov rax, qword ptr [rdi + 0x8eb8]
003563B2  0F BE 4B 24                     movsx ecx, byte ptr [rbx + 0x24]
003563B6  48 85 C0                        test rax, rax
003563B9  75 6C                           jne 0x140356427
003563BB  F6 43 23 01                     test byte ptr [rbx + 0x23], 1
003563BF  48 8B 7C 24 50                  mov rdi, qword ptr [rsp + 0x50]
003563C4  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
003563C9  74 0C                           je 0x1403563d7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_003563AB(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10)
{
}
```

## 5. (Beta) C Style

```c
int64_t sub_003563AB(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, int64_t Arg9, int64_t Arg10)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003563AB&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003563AB[BB_003563AB]
  bb_003563BB[BB_003563BB]
  bb_003563AB -->|fallthrough| bb_003563BB
```
