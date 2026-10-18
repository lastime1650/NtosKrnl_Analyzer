# AstInitializeBloomFilter

- RVA: `0x00722E34`–`0x00722E51` (길이 `29` bytes)
- VA: `0x0000000140722E34`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `5`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [IoInitSystemPreDrivers](../../init/C2/IoInitSystemPreDrivers_function_00C2AC3C.md) at `0x00C2B5DE`

### Static image references
- `0x00722E34` → RVA `0x00F8D050` (`.data`; write)
- `0x00722E3E` → RVA `0x00F8D040` (`.data`; write)
- `0x00722E48` → RVA `0x00F8D048` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00722E34  C7 05 12 A2 86 00 8B FD 56 CD   mov dword ptr [rip + 0x86a212], 0xcd56fd8b
00722E3E  C7 05 F8 A1 86 00 00 80 00 00   mov dword ptr [rip + 0x86a1f8], 0x8000
00722E48  4C 89 05 F9 A1 86 00            mov qword ptr [rip + 0x86a1f9], r8
00722E4F  C3                              ret
00722E50  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall AstInitializeBloomFilter(__int64 a1, __int64 a2, __int64 a3)
{
    *(unsigned int *)(v_rip + 8823314) = 0xCD56FD8BULL;
    *(unsigned int *)(v_rip + 8823288) = 0x8000ULL;
    *(unsigned __int64 *)(v_rip + 8823289) = a3;
    return;
}
```

## 5. (Beta) C Style

```c
void AstInitializeBloomFilter(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    *(uint32_t *)(v_rip + 0x86A212) = 0xCD56FD8BULL;
    *(uint32_t *)(v_rip + 0x86A1F8) = 0x8000ULL;
    *(uint64_t *)(v_rip + 0x86A1F9) = Arg3;
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00722E34&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00722E34[BB_00722E34]
  bb_00722E50[BB_00722E50]
```
