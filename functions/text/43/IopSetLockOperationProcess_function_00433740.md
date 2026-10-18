# IopSetLockOperationProcess

- RVA: `0x00433740`–`0x00433766` (길이 `38` bytes)
- VA: `0x0000000140433740`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A25E8`
- 디코드: `13`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [IopCloseFile](../../page/86/IopCloseFile_function_008640C0.md) at `0x008642F6`
- [NtLockFile](../../page/9D/NtLockFile_function_009D86D0.md) at `0x009D88C4`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00433760` → [sub_0043399C](Unknown_function_0043399C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00433740  40 56                           push rsi
00433742  57                              push rdi
00433743  41 54                           push r12
00433745  41 55                           push r13
00433747  41 57                           push r15
00433749  48 83 EC 20                     sub rsp, 0x20
0043374D  45 33 ED                        xor r13d, r13d
00433750  45 32 E4                        xor r12b, r12b
00433753  41 0F B6 F0                     movzx esi, r8b
00433757  4C 8B FA                        mov r15, rdx
0043375A  48 8B F9                        mov rdi, rcx
0043375D  48 85 D2                        test rdx, rdx
00433760  0F 84 36 02 00 00               je 0x14043399c
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall IopSetLockOperationProcess(__int64 a1, __int64 a2, unsigned __int8 a3)
{
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    v_r13 = 0;
    v_r12 = 0;
}
```

## 5. (Beta) C Style

```c
void IopSetLockOperationProcess(int64_t Arg1, int64_t Arg2, uint8_t Arg3)
{
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    local_r13 = 0;
    local_r12 = 0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00433740&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00433740[BB_00433740]
```
