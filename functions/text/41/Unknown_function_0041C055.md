# sub_0041C055

- RVA: `0x0041C055`–`0x0041C08D` (길이 `56` bytes)
- VA: `0x000000014041C055`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009D6E0`
- 디코드: `15`개 명령, `56/56` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0041C074` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0041C063` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0041C055  F0 81 66 30 FC FF FF 7F         lock and dword ptr [rsi + 0x30], 0x7ffffffc
0041C05D  40 80 FF 11                     cmp dil, 0x11
0041C061  74 1E                           je 0x14041c081
0041C063  83 3D B6 AC BA 00 00            cmp dword ptr [rip + 0xbaacb6], 0
0041C06A  74 0D                           je 0x14041c079
0041C06C  44 0F 20 C1                     mov rcx, cr8
0041C070  40 0F B6 D7                     movzx edx, dil
0041C074  E8 1F 96 0D 00                  call 0x1404f5698
0041C079  40 0F B6 C7                     movzx eax, dil
0041C07D  44 0F 22 C0                     mov cr8, rax
0041C081  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
0041C086  48 83 C4 20                     add rsp, 0x20
0041C08A  5F                              pop rdi
0041C08B  C3                              ret
0041C08C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0041C055(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8)
{
    __int64 result;
    __int64 v_rsp;

    if (((unsigned __int8)(v_rdi)) == 17) goto loc_0041C081;
    if ((*(unsigned int *)(v_rip + 12233910)) != 0) {
        a1 = v_cr8;
        a2 = (unsigned __int8)(v_rdi);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
loc_0041C081:
    v_rsp = (v_rsp) + (32);
    return (unsigned __int8)(v_rdi);
}
```

## 5. (Beta) C Style

```c
int64_t sub_0041C055(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, int64_t Arg8)
{
    int64_t result;
    int64_t local_rsp;

    if (((uint8_t)(local_rdi)) == 17) goto loc_0041C081;
    if ((*(uint32_t *)(v_rip + 0xBAACB6)) != 0) {
        Arg1 = v_cr8;
        Arg2 = (uint8_t)(local_rdi);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg4);
    }
loc_0041C081:
    local_rsp = (local_rsp) + (32);
    return (uint8_t)(local_rdi);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0041C055&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0041C055[BB_0041C055]
  bb_0041C063[BB_0041C063]
  bb_0041C06C[BB_0041C06C]
  bb_0041C079[BB_0041C079]
  bb_0041C081[BB_0041C081]
  bb_0041C08C[BB_0041C08C]
  bb_0041C055 -->|branch| bb_0041C081
  bb_0041C055 -->|fallthrough| bb_0041C063
  bb_0041C063 -->|branch| bb_0041C079
  bb_0041C063 -->|fallthrough| bb_0041C06C
  bb_0041C06C -->|flow| bb_0041C079
  bb_0041C079 -->|flow| bb_0041C081
```
