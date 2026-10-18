# IoGetOplockKeyContextEx

- RVA: `0x003F36C0`–`0x003F36E8` (길이 `40` bytes)
- VA: `0x00000001403F36C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `14`개 명령, `40/40` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [FsRtlpOplockKeysEqual](FsRtlpOplockKeysEqual_function_003F26B0.md) at `0x003F27F2`
- [FsRtlpOplockStoreKeyForDeleteOperation](FsRtlpOplockStoreKeyForDeleteOperation_function_003F2A90.md) at `0x003F2B0D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003F36C0  48 8B 89 D0 00 00 00            mov rcx, qword ptr [rcx + 0xd0]
003F36C7  48 85 C9                        test rcx, rcx
003F36CA  74 18                           je 0x1403f36e4
003F36CC  48 8B 49 38                     mov rcx, qword ptr [rcx + 0x38]
003F36D0  48 85 C9                        test rcx, rcx
003F36D3  74 0F                           je 0x1403f36e4
003F36D5  F6 41 02 03                     test byte ptr [rcx + 2], 3
003F36D9  B8 00 00 00 00                  mov eax, 0
003F36DE  48 0F 45 C1                     cmovne rax, rcx
003F36E2  C3                              ret
003F36E3  CC                              int3
003F36E4  33 C0                           xor eax, eax
003F36E6  C3                              ret
003F36E7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoGetOplockKeyContextEx(__int64 a1)
{
    __int64 result;

    if (*(unsigned __int64 *)(a1 + 208) == 0) goto loc_003F36E4;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 208) + 56) == 0) goto loc_003F36E4;
    result = 0;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 208) + 56) + 2)) & (3)) != 0) { result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 208) + 56); }
    return result;
loc_003F36E4:
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IoGetOplockKeyContextEx(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if (*(uint64_t *)(arg1 + 0xD0) == 0) goto loc_003F36E4;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0xD0) + 0x38) == 0) goto loc_003F36E4;
    result = 0;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xD0) + 0x38) + 0x2)) & (3)) != 0) { result = *(uint64_t *)(*(uint64_t *)(arg1 + 0xD0) + 0x38); }
    return result;
loc_003F36E4:
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xD0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003F36C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003F36C0[BB_003F36C0]
  bb_003F36CC[BB_003F36CC]
  bb_003F36D5[BB_003F36D5]
  bb_003F36E3[BB_003F36E3]
  bb_003F36E4[BB_003F36E4]
  bb_003F36E7[BB_003F36E7]
  bb_003F36C0 -->|branch| bb_003F36E4
  bb_003F36C0 -->|fallthrough| bb_003F36CC
  bb_003F36CC -->|branch| bb_003F36E4
  bb_003F36CC -->|fallthrough| bb_003F36D5
  bb_003F36E3 -->|flow| bb_003F36E4
```
