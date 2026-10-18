# sub_005AC0A9

- RVA: `0x005AC0A9`–`0x005AC0D9` (길이 `48` bytes)
- VA: `0x00000001405AC0A9`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C9508`
- 디코드: `13`개 명령, `48/48` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005AC0C5` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005AC0A9  40 0F B6 C7                     movzx eax, dil
005AC0AD  24 07                           and al, 7
005AC0AF  88 06                           mov byte ptr [rsi], al
005AC0B1  48 FF C6                        inc rsi
005AC0B4  48 C1 ED 03                     shr rbp, 3
005AC0B8  48 85 ED                        test rbp, rbp
005AC0BB  74 17                           je 0x1405ac0d4
005AC0BD  4C 8B C5                        mov r8, rbp
005AC0C0  B2 82                           mov dl, 0x82
005AC0C2  48 8B CE                        mov rcx, rsi
005AC0C5  E8 76 AB 11 00                  call 0x1406c6c40
005AC0CA  48 BA 00 00 00 00 00 80 FF FF   movabs rdx, 0xffff800000000000
005AC0D4  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_005AC0A9(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rsi;

    result = (unsigned __int8)(((unsigned __int8)(v_rdi)) & (7));
    *(unsigned __int8 *)(v_rsi) = (unsigned __int8)(result);
    v_rsi = (v_rsi) + 1;
    v_rbp = (v_rbp) >> (3);
    if (v_rbp != 0) {
        a3 = v_rbp;
        a2 = 130;
        a1 = v_rsi;
        result = memset(a1, a2, a3, a4);
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_005AC0A9(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, int64_t Arg11)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rsi;

    result = (uint8_t)(((uint8_t)(local_rdi)) & (7));
    *(uint8_t *)(local_rsi) = (uint8_t)(result);
    local_rsi = (local_rsi) + 1;
    local_rbp = (local_rbp) >> (3);
    if (local_rbp != 0) {
        Arg3 = local_rbp;
        Arg2 = 130;
        Arg1 = local_rsi;
        result = memset(Arg1, Arg2, Arg3, Arg4);
    }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005AC0A9&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005AC0A9[BB_005AC0A9]
  bb_005AC0BD[BB_005AC0BD]
  bb_005AC0D4[BB_005AC0D4]
  bb_005AC0A9 -->|branch| bb_005AC0D4
  bb_005AC0A9 -->|fallthrough| bb_005AC0BD
  bb_005AC0BD -->|flow| bb_005AC0D4
```
