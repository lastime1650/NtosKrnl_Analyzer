# CmCloseRmHandle

- RVA: `0x00702DD8`–`0x00702DF5` (길이 `29` bytes)
- VA: `0x0000000140702DD8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [CmpTryToRundownHive](../../text/2A/CmpTryToRundownHive_function_002A4A60.md) at `0x002A4B88`
- [CmShutdownSystem1](../../text/66/CmShutdownSystem1_function_0066A5B0.md) at `0x0066A60B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00702DD8  33 C0                           xor eax, eax
00702DDA  48 85 C9                        test rcx, rcx
00702DDD  74 14                           je 0x140702df3
00702DDF  83 79 40 01                     cmp dword ptr [rcx + 0x40], 1
00702DE3  74 05                           je 0x140702dea
00702DE5  80 FA 01                        cmp dl, 1
00702DE8  75 09                           jne 0x140702df3
00702DEA  48 8B 41 30                     mov rax, qword ptr [rcx + 0x30]
00702DEE  48 83 61 30 00                  and qword ptr [rcx + 0x30], 0
00702DF3  C3                              ret
00702DF4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmCloseRmHandle(__int64 a1, unsigned __int8 a2)
{
    __int64 result;

    result = 0;
    if (a1 == 0) goto loc_00702DF3;
    if ((*(unsigned int *)(a1 + 64)) == 1) goto loc_00702DEA;
    if (a2 == 1) {
        result = *(unsigned __int64 *)(a1 + 48);
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmCloseRmHandle(int64_t Arg1, uint8_t Arg2)
{
    int64_t result;

    result = 0;
    if (Arg1 == 0) goto loc_00702DF3;
    if ((*(uint32_t *)(Arg1 + 0x40)) == 1) goto loc_00702DEA;
    if (Arg2 == 1) {
        result = *(uint64_t *)(Arg1 + 0x30);
    }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00702DD8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00702DD8[BB_00702DD8]
  bb_00702DDF[BB_00702DDF]
  bb_00702DE5[BB_00702DE5]
  bb_00702DEA[BB_00702DEA]
  bb_00702DF3[BB_00702DF3]
  bb_00702DF4[BB_00702DF4]
  bb_00702DD8 -->|branch| bb_00702DF3
  bb_00702DD8 -->|fallthrough| bb_00702DDF
  bb_00702DDF -->|branch| bb_00702DEA
  bb_00702DDF -->|fallthrough| bb_00702DE5
  bb_00702DE5 -->|branch| bb_00702DF3
  bb_00702DE5 -->|fallthrough| bb_00702DEA
  bb_00702DEA -->|flow| bb_00702DF3
```
